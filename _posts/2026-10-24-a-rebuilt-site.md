---
title: "A rebuilt site, and why the publication list is now generated"
date: 2026-10-24
description: >-
  The site is now built from structured data rather than hand-edited HTML, and
  the publication list is regenerated from OpenAlex instead of maintained by
  hand.
tags: [open science, meta]
---

The old version of this site kept every publication, course and award inside
the HTML of seven separate pages. That has two failure modes, and both of them
had already happened: entries drift out of date because updating them means
editing markup, and content from the template a site was forked from can sit
there unnoticed for years.

Everything is now held in `_data/*.yml`. A course is a two-line YAML entry. An
award is three. The publication list is not written by hand at all — it is
generated from my [OpenAlex](https://openalex.org) record by a script in the
repository, so adding a paper means running one command.

Two deliberate constraints:

1. **Corrections are separate from generated data.** OpenAlex attributes a
   handful of materials-science papers to me through a name collision. Those
   DOIs are listed in `_data/pub_overrides.yml`, which the generator reads and
   never rewrites, so the correction survives every refresh.
2. **Quartile labels come from a source, not an estimate.** Journal quartiles
   live in their own file with the ranking edition they were taken from. There
   is no automatic inference, because a plausible-looking guess on a CV is
   worse than no label at all.

The source is on [GitHub](https://github.com/babasaraki/babasaraki.github.io)
if any of it is useful to you.
