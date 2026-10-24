# babasaraki.github.io

Personal academic site for **Umar Ahmad, PhD** — Senior Genomic Scientist.
Built with Jekyll and published by GitHub Pages at
<https://babasaraki.github.io>.

The site is driven by structured data: almost nothing you will want to change
lives in HTML. Add a paper, a course or an award by editing one YAML file.

---

## Where things live

| You want to change… | Edit |
|---|---|
| Name, role, bio strapline, photo, social links, email, address | `_data/profile.yml` |
| The four research strands and the skills grid | `_data/research.yml`, `_data/profile.yml` |
| Jobs and appointments | `_data/employment.yml` |
| Degrees and training | `_data/education.yml` |
| Courses, invited talks, workshops | `_data/teaching.yml` |
| Service, memberships, awards | `_data/activities.yml` |
| Journal quartiles (Q1–Q4 badges) | `_data/journal_quartiles.yml` |
| Publication corrections and featured papers | `_data/pub_overrides.yml` |
| The publication list itself | **generated** — see below |
| Navigation menu | `_data/nav.yml` |
| Site title, description, URL | `_config.yml` |
| Colours, type, spacing | the `:root` block in `assets/css/style.scss` |
| Blog posts | add a file to `_posts/` |

## Updating publications

`_data/publications.yml` is **generated** — do not edit it by hand, your
changes will be overwritten. Instead:

```bash
pip install -r scripts/requirements.txt
export OPENALEX_API_KEY=...          # free key from https://openalex.org
python scripts/update_publications.py
```

The script pulls every work attributed to OpenAlex author
[`A5016908264`](https://openalex.org/A5016908264), removes the DOIs listed under
`exclude:` in `_data/pub_overrides.yml`, collapses duplicate records (a preprint
whose journal version is also present is dropped), merges the hand-written
entries under `extra:`, and rewrites `_data/publications.yml` together with the
citation metrics shown on the home page.

Run it a few times a year, or whenever a paper lands. Commit the result.

### Correcting the record

OpenAlex attributes a few materials-science papers to you through a name
collision with another Ahmad Umar. Those DOIs are already in the `exclude:`
list. If you spot another, add its DOI there — the overrides file is never
rewritten by the script, so corrections survive every refresh.

Work OpenAlex does not index (books, local conference proceedings, journals
outside its coverage) goes under `extra:` in the same file.

## Journal quartiles

`_data/journal_quartiles.yml` is the **only** place the site reads Q1/Q2/Q3/Q4
from. Nothing is inferred: a journal with an empty `quartile:` simply renders
without a badge, and the quartile filter on the publications page only appears
once at least one value is set.

Fill in each journal's best quartile from SCImago, Scopus or JCR, record which
subject category it came from, and set the `source:` and `year:` at the top of
the file so the page can state its provenance. Re-check annually.

Once any Q1 or Q2 journal is filled in, the home page automatically switches its
"Selected work" block from the hand-picked `featured:` DOIs to your Q1/Q2
journal articles.

## Local preview

Optional — GitHub Pages builds the site without any of this.

```bash
bundle install
bundle exec jekyll serve --livereload
# http://127.0.0.1:4000
```

Requires Ruby 3.x. If `bundle install` fails on `nokogiri`, install your
platform's build tools first.

## Deploying

The site builds natively on GitHub Pages — no Actions workflow and no local
toolchain needed, because it uses only whitelisted plugins (`jekyll-feed`,
`jekyll-seo-tag`, `jekyll-sitemap`).

1. Push to the `main` branch of `babasaraki/babasaraki.github.io`.
2. Repository **Settings → Pages → Build and deployment → Source: Deploy from a branch**, branch `main`, folder `/ (root)`.
3. Wait a minute; the build status appears under the **Actions** tab.

Do **not** add a `.nojekyll` file — it disables the build and serves raw source.

## Things to fill in

- `_data/employment.yml` — the start year for the Directorate of Linkages role
  is marked `TODO`.
- `_data/journal_quartiles.yml` — quartiles for 24 journals.
- `assets/cv/umar-ahmad-cv.pdf` — drop a PDF here and a download button appears
  on the CV page. Remove `cv_pdf:` from `_data/profile.yml` if you would rather
  not have one.

## What changed from the previous site

- The publications page listed a block of coffee, blueberry and clover genetics
  papers by L. F. V. Ferrão, inherited from the template the old site was forked
  from. Removed.
- The education page linked "Professor Abhi Veerakumarasivam" and the site-wide
  Google Scholar button to two different Scholar profiles. The supervisor link is
  kept on his own profile; the site-wide link now points at yours only.
- Three of your papers that were on the old site are not indexed in OpenAlex and
  would have been lost by an automated rebuild; they are preserved under
  `extra:` in `_data/pub_overrides.yml`.
- No CDN dependencies. The old site loaded Tailwind/Flowbite and Google Fonts
  from third-party CDNs on every page view; the CSS is now self-hosted and the
  type uses a system font stack.
- Dark mode, keyboard-accessible navigation, a skip link, print styles for the
  CV page, `schema.org/Person` structured data, sitemap and RSS feed.

## Licence

Site code: MIT (`LICENSE`). Written content and figures: CC BY 4.0.
