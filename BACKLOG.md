# Wofchuck Honey Co. — Backlog

One phase per session. Pick the top unchecked phase and do it.
Context: [`PRODUCT_BRIEF.md`](PRODUCT_BRIEF.md) and [`TECH_DESIGN.md`](TECH_DESIGN.md).

---

## Where we are (2026-10-26, end of session)

- **State:** the one-page demo is done and committed on `main` (not pushed).
  The contact form is built but **switched off** (`FORM_ON = false` in
  `index.html`): Send shows "This is a preview…" everywhere. The Worker exists
  in `worker/` (15 tests green) but isn't deployed.
- **Waiting on Bill:** run `/code-review`, push, and turn on GitHub Pages
  (phase P below), then send Mike the github.io link. Also ask Mike the open
  questions in `PRODUCT_BRIEF.md`.
- **Next task for a session:** after Pages is up, **F3**. Phase 2 is blocked
  on Mike's answers.

### P — Put the demo on GitHub Pages (Bill, by hand)
- [ ] `/code-review` on `main` before the first push
- [ ] github.com → New repository → name `wofchuck-honey-website`, **Public**,
      no README (the repo already has one). Then in Terminal, in this folder:
      `git remote add origin https://github.com/billparnell/wofchuck-honey-website.git`
      and `git push -u origin main`
- [ ] Repo → Settings → Pages → Source "Deploy from a branch", Branch `main`,
      folder `/ (root)` → Save. Wait 1–2 minutes.
- [ ] Open `https://billparnell.github.io/wofchuck-honey-website/`. Check
      `…/BACKLOG.html` is a 404 (the `_config.yml` excludes worked).
- [ ] Send Mike that link. Write the real URL into `TECH_DESIGN.md`.

### Phase 1 — Demo for Mike — ✅ DONE 2026-10-26
- [x] Pull content from the 8 archived Weebly pages in `raw_input/`
- [x] Trace the label into SVGs (`tools/make_logo.py`)
- [x] One-page site: story, honey, stores, pairings, order, contact
- [x] Checked at 375px and 1280px in headless Chrome
- [x] Private demo link published for Bill to send to Mike:
      https://claude.ai/artifact/BmkYrYZR5Gb3zmfWRS3dAp (share it from the page's
      Share menu). To update it: copy `index.html` minus the doctype/html/head/body
      tags plus `css/` and `img/` into a scratch folder and republish to that URL.

### Phase 2 — Mike's answers (blocked on Mike)
- [ ] Go through the open questions in `PRODUCT_BRIEF.md` with Mike
- [ ] Apply his edits to copy, honey list and store list
- [ ] Add his photos (story section and hero are the natural places) and a
      high-res logo if he has one

## Contact form (decided 2026-10-26: form, not a published email)

### F1 — Worker — ✅ DONE 2026-10-26
- [x] Copied wolfthump's Worker into `worker/`, renamed to `wofchuck-contact`,
      new wording; 15 tests pass (`node --test worker/contact.test.mjs`)

### F2 — Form on the page — ✅ DONE 2026-10-26
- [x] Name/email/message form replaces the shown email; honeypot, timer,
      Turnstile (test key), thank-you card, preview note on the demo link
- [x] Checked at 375px in headless Chrome: fields 56px, text 18px, no
      overflow; live path shows a clean error (Worker not deployed yet)
- [x] `FORM_ON` switch, off for now, so Mike's github.io preview shows a note
      rather than a "did not go through" error
- [x] Top bar: text name from 640px up, links only on phones

### F3 — GitHub Pages + accounts + deploy (needs Bill's hands)
- [ ] After phase P: fix the github.io origin in `worker/wrangler.jsonc` if
      it differs from `https://billparnell.github.io`.
- [ ] Cloudflare → Turnstile → new widget, hostnames = the github.io host +
      wofchuckhoneyco.com. Site key into `index.html` (replaces the test key);
      secret key → Worker secret.
- [ ] Resend → new API key for this app only (PLAYBOOK §3).
- [ ] `npx wrangler deploy -c worker/wrangler.jsonc`; confirm it answers 503
      "not switched on yet" with curl.
- [ ] Bill, in his own Terminal: `npx wrangler secret put <NAME> -c worker/wrangler.jsonc`
      for TURNSTILE_SECRET, RESEND_API_KEY, MAIL_TO (his Gmail), MAIL_FROM
      (`Wofchuck Honey Co. <wofchuck@parnellprojects.com>`).
- [ ] Check `CONTACT_URL` in `index.html` matches the deployed Worker.
- [ ] **Set `FORM_ON = true` in `index.html`** only once the Worker answers
      with all secrets set. Then republish the claude.ai demo copy too.

### F4 — End-to-end and review
- [ ] Real submission from the live page on a phone: inquiry arrives, Reply-To
      works, confirmation arrives and isn't in spam.
- [ ] Live curls as in wolfthump's Phase 4 (bad token 400, foreign Origin 403,
      honeypot fake 200, GET 405, preflight 204).
- [ ] **`/security-review` before the form is announced.**

### Phase 4 — Go live on wofchuckhoneyco.com
- [ ] Find out where the domain's DNS lives (NameSilo like wolfthump?)
- [ ] `CNAME` file, DNS rows as in wolfthump's TECH_DESIGN
- [ ] PNG favicon / apple-touch-icon (Safari ignores SVG favicons)
- [ ] Check on Bill's iPhone 13 mini

## Log
- 2026-10-26 (wrap): added the `FORM_ON` switch (off) so the github.io demo
  doesn't show a send error; Pages steps written up as phase P. Tests 15/15.
- 2026-10-26: Contact form F1 + F2 done; demo link republished. Next: F3.
- 2026-10-26: Phase 1 done. Store list added from `raw_input/store_locations.png`. The old site's photos aren't on archive.org (404).
