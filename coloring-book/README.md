# Fun Adventures & Cute Animals — Coloring Book (ages 3–8)

30 print-ready, black-and-white line-art coloring pages.

## Print files (`output/`)

| File | Use |
|---|---|
| `Fun-Adventures-and-Cute-Animals-Coloring-Book-Letter.pdf` | 30 pages, US Letter (8.5 × 11 in) portrait, vector (prints crisp at any DPI) |
| `Fun-Adventures-and-Cute-Animals-Coloring-Book-A4.pdf` | 30 pages, A4 (210 × 297 mm) portrait, vector, centred |
| `png-300dpi/NN_name.png` | One page per file, 2550 × 3300 px = US Letter at 300 DPI |
| `../svg/NN_name.svg` | Editable vector source for every page |

Specs: pure white `#FFFFFF` background, pure black `#000000` outlines (≈ 5.8 pt bold
outlines, ≈ 4 pt inner details), no shading/greys/textures, no text, page numbers or
watermarks, ≥ 0.75 in white margins, one illustration per page.

**Printing tip:** choose "Actual size" / 100 % (not "Fit"), single-sided, so kids can
use markers without bleed-through.

## Rebuilding

Requires Python 3 + Pillow and Node with Playwright/Chromium.

```bash
python3 build.py          # all pages -> svg/, PNGs and both PDFs
python3 build.py 5 12     # only pages 5 and 12 (PDFs still include every page)
```

Each page lives in `pages/pNN_*.py` and is drawn with the small toolkit in `lib.py`
(every shape is white-filled with a black outline, layered back-to-front).
