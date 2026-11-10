# Zhiyang Liao · Academic homepage

Website: https://liaozhiyang-0.github.io/
Source: https://github.com/liaozhiyang-0/liaozhiyang-0.github.io

A bilingual, responsive academic homepage. Plain HTML, CSS, and JavaScript; no build step, package installation, external fonts, tracking, or backend. English is the default. With JavaScript disabled, the full English content remains readable.

## Preview and verify

From this repository's root (Python 3 and Node.js required only for local checks):

```sh
python tests/verify.py
node tests/language.cjs
python -m http.server 8000 --bind 127.0.0.1
```

Open http://127.0.0.1:8000. Check both languages, keyboard navigation, and narrow and wide screens. Stop the server with Ctrl+C. Checks validate structure, internal anchors, local assets, metadata, and repeated language switching. They do not verify biographical claims or external websites.

## Files and editing

- `index.html`: profile, research interests, selected projects, affiliation, and metadata. Every translated element has `data-en` and `data-zh`; its initial text must match English. Use HTML entities in attributes where needed.
- `styles.css`: layout, responsive rules, focus states, print styling.
- `script.js`: language switch, with no storage or network requests.
- `assets/mark.svg`: text-based favicon.
- `tests/`: dependency-free structural and interaction checks.

To add a project, copy an existing project article and update both languages. To add public papers later, insert a semantic section with a heading and an anchored navigation link; list only public bibliographic information and verified public URLs. No publication framework or database is needed.

## GitHub Pages

Use a public repository named `<username>.github.io`. In **Settings → Pages → Build and deployment**, select **Deploy from a branch**, `main`, and `/ (root)`. GitHub publishes each push automatically. `.nojekyll` keeps the site buildless.

After updates, verify the Pages build and the HTTPS URL. The canonical link and `og:url` in `index.html` point to the address above; update both if the hosting address changes. See [GitHub's publishing-source documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

Routine update:

```sh
python tests/verify.py
node tests/language.cjs
git add index.html styles.css script.js assets README.md tests .nojekyll .gitignore .gitattributes
git commit -m "Update academic homepage"
git push origin main
```

## Content review before first publication

- Confirm the exact English name against the owner's academic profile, then update the visible name, title, description, Open Graph metadata, footer, and accessible home label together.
- Confirm ownership of the destination GitHub account and any project repository before linking it.
- Add an academic email or ORCID only when confirmed public; the current contact section lists only the institution.
- Awards are omitted until certificates establish official names, years, and levels. Performance figures are omitted until original reports establish the measurements.
- Do not add private contact details, student IDs, grades, internal company materials, private datasets, or confidential research.

The owner confirmed the name Zhiyang Liao / 廖志洋, HUST Electronic Information Engineering enrollment in 2024, TiGPU and data modeling experience, and medical image analysis experience. Medical imaging is described only in general terms. No awards, publication claims, benchmark numbers, email address, or ORCID are included in this version.
