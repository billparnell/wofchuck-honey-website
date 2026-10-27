# Wofchuck Honey Co. — Tech & Design

## Stack
- One static page: `index.html` + `css/site.css` + SVGs in `img/`. No build
  step, no JS framework; one inline script for the contact form.
- **Contact form backend:** a Cloudflare Worker, `worker/contact.mjs`, to be
  deployed by hand as `wofchuck-contact.bparnell.workers.dev`. Email through the
  Resend HTTP API.
- Planned hosting: same as wolfthump.com, **GitHub Pages** with a `CNAME` for
  wofchuckhoneyco.com (see `../wolfthump-website/TECH_DESIGN.md` for the DNS
  rows and the Pages gotchas). Where the domain's DNS lives is not known yet.
- `_config.yml` keeps docs, `raw_input/`, `tools/` and `worker/` off the
  published site. The repo will be public, so **never commit a secret**.
  Add any new non-site file at the root to its `exclude:` list.
- **Bump `?v=` on the stylesheet link whenever `site.css` changes** (Pages
  caches CSS for 10 minutes; wolfthump lesson).

## The logo
`raw_input/logo.jpg` is a 436px scan of the jar label, too soft for a phone
screen. `tools/make_logo.py` upscales it, thresholds it and traces it to vector
with `potracer`, printing it in the site's teal:
- `img/emblem.svg`: arc text, WILDFLOWER banner, flower-bee and the wordmark
  (corner fleurons, the black ribbon and contact lines left off).
- `img/favicon.svg`: just the bee from the middle, on a pale round. (It was
  also the top-bar icon until 2026-10-26; at 40px nobody could tell what it was.)

Run: `.venv/bin/python tools/make_logo.py` (venv needs `pillow potracer`).
The ink colour is baked into the SVGs (an `<img>` can't inherit CSS colour):
**if `--ink` changes, change `INK` in the script and re-run.**
Gotcha: potracer traces the *dark* pixels of a 1-bit image; feeding it ink as
white traced the background and gave a solid teal block.

A high-res logo from Mike would replace all of this.

## Contact form

**Copied from wolfthump on 2026-10-26** (`../wolfthump-website/worker/`), with
only names and wording changed. Its `TECH_DESIGN.md` "Booking form" section has
the full table of checks and why each one exists; they're identical here:
config present (503) → Origin in `ALLOWED_ORIGINS` (403) → rate limit 3/min/IP
(429, loose by design) → body ≤20 KB + valid JSON → honeypot `website` empty and
`elapsed` ≥3 s (else **fake 200, nothing sent**) → field validation (400) →
Turnstile verified server-side (400). Then the inquiry goes to `MAIL_TO` with
Reply-To = the sender, and a **fixed-text** confirmation goes to the sender
(nothing they typed, Reply-To only `MAIL_REPLY_TO`, never `MAIL_TO`).
If a fix lands in one Worker, port it to the other.

**Config:** secrets listed at the top of `worker/contact.mjs`
(`RESEND_API_KEY`, `TURNSTILE_SECRET`, `MAIL_TO`, `MAIL_FROM`, optional
`MAIL_REPLY_TO`); `ALLOWED_ORIGINS` and the rate limit (`namespace_id` 4102;
wolfthump has 4101) are in `worker/wrangler.jsonc`. The github.io origin there is
a guess until the GitHub repo exists.

**The page side:** the script at the bottom of `index.html` does the same
empty/email/Turnstile checks before sending, POSTs
`{name,email,message,website,elapsed,turnstile}` to `CONTACT_URL`, then swaps
the form for the thank-you card. On an error it shows the Worker's message,
keeps what they typed, and resets Turnstile (tokens are single-use).
- **`FORM_ON = false` until the Worker is deployed** (set it to `true` in F3).
  While it's off, Send shows "This is a preview. The form will work once the
  site is live." everywhere, so Mike looking at the github.io page sees a note,
  not a "did not go through" error from a Worker that doesn't exist.
- With it on, `LIVE` is true only on wofchuckhoneyco.com, github.io and
  localhost. Anywhere else (the claude.ai demo) Send still shows the preview
  note: that host's security policy blocks Turnstile and the Worker.
- **Turnstile site key is the test key `1x00000000000000000000AA`** until the
  real widget exists (BACKLOG F3).
- Email field has `autocapitalize="none"` and `inputmode="email"` (PLAYBOOK's
  iOS note).

## Demo link on claude.ai (2026-10-26)
https://claude.ai/artifact/BmkYrYZR5Gb3zmfWRS3dAp, private; shared from its
Share menu. The artifact host wraps the page in its own `<html>/<head>/<body>`,
so the published copy is `index.html` with those wrapper lines removed, plus
`css/` and `img/`, republished to the same URL. Once GitHub Pages is up, that's
the better link to send.

## Visual system
Tokens on `:root` in `css/site.css`. Light only, by choice.
- **Colour:** `--paper` sea-glass white ground, `--mist` alternate bands,
  `--ink` label teal for logo/headings/buttons, `--ink-deep` footer and hover,
  `--honey` the one warm accent (pull-quote rule, "our own hives" pill, focus
  ring). Five `--jar-*` colours, one per honey, darkest to lightest.
- **Type:** Young Serif (display, echoes the label's chunky wordmark), Figtree
  body at 18px. Small-caps eyebrows nod to "PLEASE THANK THE BEES".
- **Layout:** `--col` 680px for reading text, `--wide` 1040px for grids.
  Full-width bands; `.wave` SVGs make the seams between them.
- **Components:** one `.card` family (honey and order cards), one `.pill`
  (where a honey comes from; `.pill--ours` in honey), one `.btn` family
  (`--solid`, `--line`), all ≥56px tall. `.drop` is a honey drop in a jar
  colour; `.icon` is the line-icon style for the order cards (1.7 stroke, round
  caps). New icons should match it.
- **Form:** the form and the thank-you are both a `.card`. Inputs are 56px tall
  with 18px text (under 16px iOS zooms on focus), on `--paper` inside the card.
  Errors are `--warn`, a deep honey brown; there's no red in this palette.
  Turnstile is `interaction-only`, so it takes no space unless Cloudflare wants
  a click.

## Checking it
Serve with `python3 -m http.server 8765` and drive it with headless Chrome via
`../groove-bank/tools/cdp.js` (`launch({width: 375})`; never `--window-size`,
see PLAYBOOK). 2026-10-26: no sideways scroll at 375 or 1280, fonts load, no
console errors. With `FORM_ON = true`, serving with `--bind ::` and opening
`http://[::1]:8765/` exercises the demo's preview path (that hostname isn't
`LIVE`), and `127.0.0.1` exercises the live path.

Tests: `node --test worker/contact.test.mjs` (15 tests, no dependencies).
