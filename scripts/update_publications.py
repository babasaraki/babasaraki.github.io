#!/usr/bin/env python3
"""
Regenerate _data/publications.yml from OpenAlex.

Usage
-----
    export OPENALEX_API_KEY=...          # free key from https://openalex.org
    python scripts/update_publications.py

What it does
------------
1. Pulls every work attributed to the OpenAlex author id in AUTHOR_ID.
2. Drops the DOIs listed under `exclude:` in _data/pub_overrides.yml.
3. Collapses duplicate records (preprint v1/v2, Research Square + journal
   version) keeping the most-cited copy of each title within a type.
4. Merges the hand-written entries under `extra:`.
5. Writes _data/publications.yml, including the metric block used on the
   home page.

Nothing else in the repository is touched, and the overrides file is never
rewritten, so your manual corrections survive every refresh.
"""
from __future__ import annotations

import os
import re
import sys
import datetime
import pathlib
import unicodedata

import requests
import yaml

AUTHOR_ID = "A5016908264"          # Umar Ahmad — https://openalex.org/A5016908264
ROOT = pathlib.Path(__file__).resolve().parents[1]
OVERRIDES = ROOT / "_data" / "pub_overrides.yml"
OUT = ROOT / "_data" / "publications.yml"
API = "https://api.openalex.org"

TYPE_MAP = {
    "article": "article",
    "review": "article",
    "preprint": "preprint",
    "posted-content": "preprint",
    "book": "book",
    "book-chapter": "chapter",
    "dissertation": "thesis",
    "dataset": "dataset",
    "conference-paper": "conference",
    "proceedings-article": "conference",
}


def api_key() -> str:
    key = os.environ.get("OPENALEX_API_KEY")
    if not key:
        sys.exit("Set OPENALEX_API_KEY first (free key from https://openalex.org).")
    return key


def get(path: str, **params):
    params["api_key"] = api_key()
    r = requests.get(API + path, params=params, timeout=60)
    r.raise_for_status()
    return r.json()


# OpenAlex spells repository names out in full; these read better on a page.
VENUE_FIXES = {
    "Zenodo (CERN European Organization for Nuclear Research)": "Zenodo",
    "bioRxiv (Cold Spring Harbor Laboratory)": "bioRxiv",
    "medRxiv (Cold Spring Harbor Laboratory)": "medRxiv",
    "arXiv (Cornell University)": "arXiv",
    "Research Square (Research Square)": "Research Square",
    "Universiti Putra Malaysia Institutional Repository (Universiti Putra Malaysia)": "UPM Institutional Repository",
    "Unisa Institutional Repository (University of South Africa)": "UNISA Institutional Repository",
}


def tidy_venue(v: str) -> str:
    v = (v or "").strip()
    return VENUE_FIXES.get(v, v)


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "").lower()
    return re.sub(r"[^a-z0-9]+", "", s)


def fetch_works() -> list[dict]:
    out, cursor = [], "*"
    while cursor:
        d = get(
            "/works",
            filter=f"author.id:{AUTHOR_ID}",
            per_page=200,
            cursor=cursor,
            select="id,doi,title,publication_year,type,primary_location,"
                   "authorships,cited_by_count,open_access,biblio",
        )
        out += d["results"]
        cursor = d["meta"]["next_cursor"]
        if not d["results"]:
            break
    return out


def to_entry(w: dict) -> dict:
    loc = w.get("primary_location") or {}
    src = loc.get("source") or {}
    bib = w.get("biblio") or {}
    doi = (w.get("doi") or "").replace("https://doi.org/", "")
    entry = {
        "title": (w.get("title") or "").strip(),
        "authors": [a["author"]["display_name"] for a in w.get("authorships", [])],
        "year": w.get("publication_year"),
        "venue": tidy_venue(src.get("display_name") or ""),
        "type": TYPE_MAP.get(w.get("type", ""), "other"),
        "doi": doi,
        "url": f"https://doi.org/{doi}" if doi else (loc.get("landing_page_url") or ""),
        "citations": w.get("cited_by_count", 0),
        "oa": bool((w.get("open_access") or {}).get("is_oa")),
        "issn": src.get("issn_l") or "",
    }
    if bib.get("volume"):
        entry["volume"] = bib["volume"]
    return entry


def main() -> None:
    ov = yaml.safe_load(OVERRIDES.read_text()) or {}
    excluded = {str(d).lower().strip() for d in ov.get("exclude", [])}

    entries = []
    for w in fetch_works():
        e = to_entry(w)
        if not e["title"] or e["doi"].lower() in excluded:
            continue
        entries.append(e)

    # Collapse duplicates: same normalised title AND same type.
    best: dict[tuple, dict] = {}
    for e in entries:
        k = (norm(e["title"]), e["type"])
        cur = best.get(k)
        if cur is None or (e["citations"], e["year"] or 0) > (cur["citations"], cur["year"] or 0):
            best[k] = e
    entries = list(best.values())

    # A preprint whose journal version is already present is dropped.
    published = {norm(e["title"]) for e in entries if e["type"] in {"article", "book", "chapter", "conference"}}
    entries = [e for e in entries if not (e["type"] == "preprint" and norm(e["title"]) in published)]

    entries += ov.get("extra", []) or []
    entries.sort(key=lambda e: (-(e.get("year") or 0), e["title"].lower()))

    prof = get(f"/authors/{AUTHOR_ID}")
    stats = prof.get("summary_stats", {})
    payload = {
        "updated": datetime.date.today().isoformat(),
        "source": f"https://openalex.org/{AUTHOR_ID}",
        "metrics": {
            "works": len(entries),
            "citations": prof.get("cited_by_count", 0),
            "h_index": stats.get("h_index", 0),
            "i10_index": stats.get("i10_index", 0),
        },
        "featured": [str(d) for d in (ov.get("featured") or [])],
        "items": entries,
    }

    header = (
        "# GENERATED FILE — do not edit by hand.\n"
        "# Rebuild with:  python scripts/update_publications.py\n"
        "# Corrections belong in _data/pub_overrides.yml.\n"
    )
    OUT.write_text(header + yaml.safe_dump(payload, allow_unicode=True, sort_keys=False, width=100))
    print(f"wrote {OUT.relative_to(ROOT)} — {len(entries)} entries")


if __name__ == "__main__":
    main()
