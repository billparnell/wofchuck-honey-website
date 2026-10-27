# Wofchuck Honey Co. — Backlog

One phase per session. Pick the top unchecked phase and do it.
Context: [`PRODUCT_BRIEF.md`](PRODUCT_BRIEF.md) and [`TECH_DESIGN.md`](TECH_DESIGN.md).

---

### Phase 1 — Demo for Mike — ✅ DONE 2026-10-26
- [x] Pull content from the 8 archived Weebly pages in `raw_input/`
- [x] Trace the label into SVGs (`tools/make_logo.py`)
- [x] One-page site: story, honey, pairings, order, contact
- [x] Checked at 375px and 1280px in headless Chrome
- [x] Private demo link published for Bill to send to Mike

### Phase 2 — Mike's answers (blocked on Mike)
- [ ] Go through the open questions in `PRODUCT_BRIEF.md` with Mike
- [ ] Apply his edits to copy, honey list and store list
- [ ] Add his photos (story section and hero are the natural places) and a
      high-res logo if he has one

### Phase 3 — Contact
- [ ] Depends on Mike's answer: keep the shown email, or copy wolfthump's form
      + Cloudflare Worker (`../wolfthump-website/worker/`). A form means
      `/security-review` before it goes live.

### Phase 4 — Go live on wofchuckhoneyco.com
- [ ] Find out where the domain's DNS lives (NameSilo like wolfthump?)
- [ ] GitHub repo + Pages, `CNAME` file, DNS rows as in wolfthump's TECH_DESIGN
- [ ] PNG favicon / apple-touch-icon (Safari ignores SVG favicons)
- [ ] Check on Bill's iPhone 13 mini

## Log
- 2026-10-26: Phase 1 done. The old site's photos aren't on archive.org (404).
