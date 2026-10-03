# Flepsite - Fleptor's Website.
A personal website made by Fleptor for Fleptor,
the website is a platform for all my personal works, blog-posts and
life plans, and is my first attempt at making a static website.

For assets/resources used check out credits page.

The domain homepage is now **Places**, a directory of the public websites and
projects under `belalhamdan.com`. Arabic lives at `/` and English at `/en/`.
The original Flepsite homepages are preserved at `/flepsite/` and
`/en/flepsite/`; their existing articles, project pages, and assets retain their
original addresses.

The directory is plain HTML with shared styling in `css/places.css`. There is
no build step, JavaScript dependency, or change to DNS. GitHub Pages continues
to publish the root of `main`, and the other repositories keep their project
paths. To update the directory, edit both `index.html` and `en/index.html` and
verify destination URLs before adding them. Alternate addresses for the same
project appear under “Explore inside.” Unavailable destinations are omitted.

For local preview, run `python -m http.server 8766` from this directory and
open `http://localhost:8766/`.
