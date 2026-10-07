# Flepsite - Fleptor's Website.
A personal website made by Fleptor for Fleptor,
the website is a platform for all my personal works, blog-posts and
life plans, and is my first attempt at making a static website.

For assets/resources used check out credits page.

Flepsite's homepage welcomes visitors to Belal's web space with quick links to
websites and personal projects, and short previews of the About page. Arabic
lives at `/` and English at `/en/`. The former `/flepsite/` and `/en/flepsite/`
addresses redirect to those homepages. There is one website, not a separate
landing site and archive.

The complete works directory is `/fp/` (English: `/en/fp/`). The Flepsite card
on Home opens the GitHub repository; its card on the works page opens the
website's story at `/fp/flepsite.html` or `/en/fp/flepsite.html`.

All content pages share the original pixel-space wallpaper, fixed behind the page,
and Flepsite's blue palette and local fonts. Shared navigation, footer, and
base styling live in `css/site.css`; Home, About, and the works grid use
`css/places.css`, and project pages, blog articles, and credits use `css/archive.css`.
The two blog indexes use `css/blog.css` to retain the original sticky icon sidebar,
paired posts/pinned-post panels, compact section spacing, and regular-weight
headings. Their navigation icons are local SVGs in `assets/icons/blog-navigation.svg`.
About, Blog, and the works directory retain the large original pixel titles:
ABOUT, BLOG, and FLEPNESS PORTAL, with the blue and orange shadows.
The Discord page also keeps its original stylesheet for the handmade profile.
Headers and footers are embedded in each HTML page so navigation works without
JavaScript. The old `components/footer.html` fragment is no longer loaded.
The footer shows Belal Jamal Hamdan, the year, Contact, and Credits.
`js/site.js` updates the year, with a year already present in the HTML as a fallback.

The homepage restores the eight-step, two-second FLEPSITE typewriter animation.
The rest of the page fades in afterward. It uses CSS and works without JavaScript;
reduced-motion preferences and direct fragment links show the content immediately.

The portrait on both homepages is copied unchanged from
`flepsite-reimagined/assets/belal-portrait.webp` to `assets/files/belal-portrait.webp`.
The layout uses the original Flepsite artwork and fonts without decorative
section numbers. Arabic headings and introductions are written for Arabic
readers rather than translated literally from English.

There is no build step or change to DNS. GitHub Pages continues
to publish the root of `main`, and the other repositories keep their project
paths. To update the quick links, edit both `index.html` and `en/index.html`,
and keep the complete works directory in both `fp/index.html` files up to date.
Home has no expandable lists of extra links. Project routes served by other
repositories, such as `/Fleptix/`,
will only resolve on the public domain, not from this repository's local preview.

The About pages, `about.html` and `en/about.html`, collect short moments from
Flepness Paradise, Flepness Broadcast, the FP ARG, the Minecraft building video,
and Belal's 2025/2026 LinkedIn recap. The older entries are trimmed from their
original Arabic and English pages; the LinkedIn entries retain the Arabic
wording where possible, with English translations. The Broadcast recap omits
the older self-critical commentary. Links lead to the original pages and the
public LinkedIn profile used as the source:
<https://jo.linkedin.com/in/belal-hamdan/ar> (reviewed 7 October 2026).
The two miscellaneous pages expose `#fp-arg` and `#minecraft` anchors for these
links. Keep matching story IDs in both About pages when adding or editing a
moment. Credits for the original fonts and artwork remain on the credits page.
About dates were confirmed by Belal on 7 October 2026: Orange June–September;
Fleptix 13 September; BAU-CPC 15 September; JCPC 18–19 September; the IEEE recap
December 2025–September 2026; the ambassador role September–31 October 2026.

The website history screenshots are in `assets/files/flepsite-history/`:

- `first-attempt-2022.png`: the saved “Fleptor Static Site” from the personal
  Miscellaneous folder. Its recovery notes describe the stylesheet mapping as
  inferred from the saved HTML; no exact original creation date is known.
- `august-2022.png`: rendered from commit `acf70163c14e951724291eef84257cddf46d2566`
  (30 August 2022).
- `august-2024.png`: rendered from commit `9c5690266d8edf8ca1d4c363dcb156f60dd3d07c`
  (27 August 2024).
- `october-2026.png`: the updated homepage, captured on 7 October 2026.

Screenshots use a 1440 × 1000 viewport. Historical files were previewed from
temporary copies; the saved originals were not changed.

For local preview, run `python scripts/serve.py` from this directory and open
`http://localhost:8766/`. The preview sends `Cache-Control: no-store` for pages
and assets so edits show up immediately. If switching from the old preview
server, hard-refresh once to clear any pages already cached by the browser.
Use `--port 8767` if a different local port is needed.
