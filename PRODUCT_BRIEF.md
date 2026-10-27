# Wofchuck Honey Co. — Product Brief

## What it is
A one-page website for Wofchuck Honey Co., Mike and Colleen Wofchuck's family
honey business in Chico, CA. It replaces their old Weebly site (8 pages, pulled
from archive.org into `raw_input/`). The domain **wofchuckhoneyco.com** is
Mike's. Same Mike as wolfthump.com.

## Who it's for
Local customers, shops, people wanting gift jars or bulk buckets, and people
asking about backyard hives or pollination. Many are older and non-technical:
big tap targets, plain words, nothing hidden behind menus.

## The page's job
Show what honey they sell and where it comes from, then get people to email.

## Decisions

- **2026-10-26: One page, not eight.** The old site's pages fold in like this:
  | Old page | Now |
  |---|---|
  | Home + About Us | **Our story** section |
  | Honey | **Our honey** section, five cards |
  | Store Locations | **Where to buy** section (from `raw_input/store_locations.png`), linked from a card in Our honey |
  | Pairings | **Pairings** section, grouped by honey |
  | Bee Hives, Specialty bottles, bulk (from Home) | **Order** section, four cards |
  | Contact | **Contact** section |
- **2026-10-26: Look.** Minimal but organic, led by the jar label and Mike's
  liking for blue/teal: the label's line art traced and printed in teal, pale
  sea-glass paper, honey as the one warm colour, wavy seams between sections.
  Light only, on purpose. Details in `TECH_DESIGN.md`.
- **2026-10-26: Contact is a form, not a published email address** (Bill's
  call), so bots can't scrape an inbox. Same setup as wolfthump: a Cloudflare
  Worker behind the form, Turnstile, honeypot, timer, rate limit.
  - Fields: **name, email, message**. Kept minimal on purpose.
  - After sending: "Thanks! We'll be in touch soon." **Don't name Mike**; someone
    else may answer.
  - The sender gets a short fixed confirmation email.
  - **Messages go to Bill's Gmail until Mike says which address he wants.**
  - Sender: `Wofchuck Honey Co. <wofchuck@parnellprojects.com>` (shared
    verified domain, no DNS work), as with wolfthump.
  - On the claude.ai demo link the form can't work (that host blocks Turnstile
    and the Worker), so Send says "This is a preview. The form will work once
    the site is live."
- **2026-10-26: Top bar shows the name as text, not the bee.** The cropped bee
  was unreadable at 40px. Phones show only the four links; the name appears
  from 640px up.
- **2026-10-26: Stores list = the old Store Locations page** (screenshot in
  `raw_input/store_locations.png`), 7 shops, each a Google Maps link. The old
  Home page said "Butte, Mendocino and Plumas counties", but the list reaches
  Auburn and Placerville, so the copy now says "from Ukiah to Placerville".
  Top nav is Honey · Stores · Order · Contact (Pairings sits right below Stores).
- **2026-10-26: Copy is lightly edited from the old site**, not rewritten.
  Typos fixed ("it's" → "its"), Mike and Colleen's bio kept, all five honeys and
  every pairing kept.

## Open questions for Mike (don't guess these)
1. **Which inbox should form messages go to?** `wofchuckhoneyco@gmail.com` (old
   Contact page), `honeyflight70@gmail.com` (jar label), or something else.
   Bill's Gmail until then.
2. **Which honeys are current?** The old Honey page lists five; the old Home
   page says "4 varieties".
3. **Store list:** is the old list still right? **Briar Patch Co-op's address
   is unreadable** in the screenshot; the page says "Address coming soon".
4. **Photos and a high-res logo.** The old site's four photos were never
   archived. The logo is traced from a 436px scan of the label.
5. **Social links** (the old site linked Facebook, but no URL survived).
6. Prices on the page, or "ask us"? The demo says ask us.

## Out of scope (for now)
- Online ordering, payments, a shop, a calendar.
- Any login or admin.
