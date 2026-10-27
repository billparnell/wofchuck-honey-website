# Wofchuck Honey Co. website

Static one-pager (`index.html`, `css/site.css`, `img/`), headed for **GitHub
Pages** on wofchuckhoneyco.com, the same setup as `../wolfthump-website`.

- Docs: `PRODUCT_BRIEF.md` (decisions, open questions for Mike),
  `TECH_DESIGN.md` (logo pipeline, visual system), `BACKLOG.md` (next phase).
- `raw_input/` is the old Weebly site from archive.org: source material only.
- Logo SVGs are generated: `.venv/bin/python tools/make_logo.py`. Don't hand-edit them.
- No tests (no logic to test). Check layout at 375px and wide with headless
  Chrome via `../groove-bank/tools/cdp.js`.
- **Bump `?v=` on the stylesheet link whenever `site.css` changes.**
- Add any new non-site root file to `_config.yml`'s `exclude:` list.
