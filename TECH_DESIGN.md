# Wofchuck Honey Co. — Tech & Design

## Stack
- One static page: `index.html` + `css/site.css` + SVGs in `img/`. No build
  step, no JS framework; one small inline script for the Copy address button.
- Planned hosting: same as wolfthump.com, **GitHub Pages** with a `CNAME` for
  wofchuckhoneyco.com (see `../wolfthump-website/TECH_DESIGN.md` for the DNS
  rows and the Pages gotchas). Where the domain's DNS lives is not known yet.
- `_config.yml` keeps docs, `raw_input/` and `tools/` off the published site.
  Add any new non-site file at the root to its `exclude:` list.
- **Bump `?v=` on the stylesheet link whenever `site.css` changes** (Pages
  caches CSS for 10 minutes; wolfthump lesson).

## The logo
`raw_input/logo.jpg` is a 436px scan of the jar label, too soft for a phone
screen. `tools/make_logo.py` upscales it, thresholds it and traces it to vector
with `potracer`, printing it in the site's teal:
- `img/emblem.svg`: arc text, WILDFLOWER banner, flower-bee and the wordmark
  (corner fleurons, the black ribbon and contact lines left off).
- `img/mark.svg`: just the bee, for the top bar. `img/favicon.svg`: the same on
  a pale round.

Run: `.venv/bin/python tools/make_logo.py` (venv needs `pillow potracer`).
The ink colour is baked into the SVGs (an `<img>` can't inherit CSS colour):
**if `--ink` changes, change `INK` in the script and re-run.**
Gotcha: potracer traces the *dark* pixels of a 1-bit image; feeding it ink as
white traced the background and gave a solid teal block.

A high-res logo from Mike would replace all of this.

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

## Checking it
Serve with `python3 -m http.server 8765` and drive it with headless Chrome via
`../groove-bank/tools/cdp.js` (`launch({width: 375})`; never `--window-size`,
see PLAYBOOK). 2026-10-26: no sideways scroll at 375 or 1280, fonts load, no
console errors.
