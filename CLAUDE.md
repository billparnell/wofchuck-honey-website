# Wofchuck Honey Co. website

Static one-pager (`index.html`, `css/site.css`, `img/`), headed for **GitHub
Pages** on wofchuckhoneyco.com, the same setup as `../wolfthump-website`.
The contact form's backend is a Cloudflare Worker in `worker/` (copied from
wolfthump's; keep fixes in step).

- Docs live in **`private/`, which is gitignored** (the repo is public):
  `private/PRODUCT_BRIEF.md` (decisions, open questions for Mike),
  `private/TECH_DESIGN.md` (logo pipeline, visual system),
  `private/BACKLOG.md` (next phase, start here), `private/BUSINESS.md`
  (pricing deal, payment log). `private/` has its own local git repo: commit
  doc changes there (`git -C private ...`). Never move them back to the root.
- `private/raw_input/` is the old Weebly site from archive.org: source only.
- Logo SVGs are generated: `.venv/bin/python tools/make_logo.py`. Don't hand-edit them.
- Tests: `node --test worker/contact.test.mjs`. No npm install, no venv needed.
- Deploy Worker: `npx wrangler deploy -c worker/wrangler.jsonc` (by hand).
  Secrets via `wrangler secret put`; the repo is public, never commit one.
- Check layout at 375px and wide with headless
  Chrome via `../groove-bank/tools/cdp.js`.
- **Bump `?v=` on the stylesheet link whenever `site.css` changes.**
- Add any new non-site root file to `_config.yml`'s `exclude:` list.
