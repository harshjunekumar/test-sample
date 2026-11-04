# Amazon KDP — Upload Guide & Listing Text

Book: **Color Me Happy!** — *Easy Coloring Book for Kids Ages 3–8* — by **Happy Crayon Press**

## Files to upload (in `output/`)

| KDP field | File |
|---|---|
| Manuscript | `Color-Me-Happy-KDP-Interior.pdf` (64 pages, 8.5 × 11 in, black & white) |
| Book cover → "Upload a cover you already have" | `Color-Me-Happy-KDP-Cover.pdf` (17.394 × 11.25 in full wrap, bleed included, spine 0.144 in) |
| Listing images, ads, social posts | `cover-front-preview.png` |

The interior has a title page, a copyright page, a "This book belongs to" page and a blank page, then the 30 pictures. Each picture is on a right-hand page with a blank back, so markers can't bleed through onto the next picture.

## Step 1 — Paperback details

- **Language:** English
- **Book title:** `Color Me Happy!`
- **Subtitle:** `Easy Coloring Book for Kids Ages 3-8 | 30 Fun Adventures & Cute Animals with Big, Bold, Simple Lines`
- **Series:** leave blank (or start one, e.g. "Happy Crayon Coloring Books", if you plan more)
- **Author:** `Happy Crayon Press`
- **Description:** paste the text below
- **Publishing rights:** "I own the copyright and I hold the necessary publishing rights"
- **Primary audience:** Sexually explicit content = **No**; Reading age **3** to **8**
- **Keywords:** the 7 boxes below
- **Categories:** see below
- **Low-content book:** leave **unticked**. A coloring book with original illustrations can use an ISBN.

### Description (paste into KDP's description box)

```
<b>Grab your crayons — a world of happy adventures is waiting!</b>

Puppies and kittens, dinosaurs and dragons, rockets, mermaids, unicorns and castles: <b>Color Me Happy!</b> is packed with 30 cheerful pictures made just for little hands.

<b>Why kids (and grown-ups) love it:</b>
<ul>
<li><b>30 original coloring pages</b> of cute animals and fun adventures</li>
<li><b>Thick, bold lines and big, simple shapes</b>, easy for small hands to color inside the lines</li>
<li><b>Friendly, smiling characters</b> with minimal backgrounds, never overwhelming</li>
<li><b>One picture per page with a blank back</b>, so markers won't bleed onto the next picture</li>
<li><b>Large 8.5 × 11 inch pages</b>, ideal for crayons, colored pencils and markers</li>
<li>Includes a <b>"This book belongs to"</b> page</li>
</ul>

Inside you'll find a playful puppy, a baby elephant, a friendly lion, a dinosaur family, a little astronaut on the moon, a happy school bus, a fairy garden, ice cream and cupcakes, a magical castle and many more!

Perfect for <b>toddlers, preschoolers and kids ages 3 to 8</b>. A great gift for birthdays, holidays, road trips, quiet time and classroom fun. Builds creativity, color recognition and fine motor skills.

<b>Scroll up and click "Buy Now" to start the coloring fun today!</b>
```

### 7 keyword boxes (one per box)

1. `coloring book for kids ages 4-8`
2. `toddler coloring book ages 2-4 big simple`
3. `cute animals coloring book for kids`
4. `easy coloring pages bold lines preschool`
5. `dinosaur unicorn puppy coloring book`
6. `kindergarten activity book boys girls gift`
7. `jumbo coloring book thick lines little kids`

### Categories (KDP lets you choose up to 3)

1. Juvenile Nonfiction › Activity Books › Coloring
2. Juvenile Nonfiction › Animals › General
3. Juvenile Nonfiction › Art › General *(or "Concepts › Colors" if offered)*

## Step 2 — Paperback content

- **ISBN:** "Get a free KDP ISBN". With the free ISBN the imprint is shown as "Independently published". To show "Happy Crayon Press" as the publisher, you need to buy your own ISBN (Bowker in the US).
- **Publication date:** leave blank
- **Print options:**
  - Ink and paper type: **Black & white interior with white paper**
  - Trim size: **8.5 × 11 in (21.59 × 27.94 cm)**
  - Bleed settings: **No Bleed**
  - Paperback cover finish: **Glossy** (bright colors pop; Matte also works)
  - Reading direction: Left to right
- **Manuscript:** upload the interior PDF
- **Book cover:** choose "Upload a cover you already have (print-ready PDF only)" and upload the cover PDF. Leave KDP's barcode option on: the bottom-right of the back cover is left clear for it.
- **AI-generated content: answer "Yes".** The illustrations, cover art and text were created with an AI tool (Claude), so select AI-generated for **images** and **text**. KDP requires this disclosure. It isn't shown to customers, but leaving it out can get the book blocked.
- Click **Launch Previewer**, page through it, then **Approve**. Fix any warnings it shows before continuing.

## Step 3 — Rights & pricing

- **Territories:** All territories (worldwide rights)
- **Primary marketplace:** Amazon.com
- **Price:** **$7.99 USD** suggested (typical range for 30–50 page kids' coloring books: $5.99–$8.99). KDP shows the exact printing cost and your royalty (60% of list price minus printing) on this screen. Keep the royalty above about $1.50 per copy.
- **Expanded Distribution:** optional (reaches more stores, but needs a higher price to stay profitable)
- Click **Publish Your Paperback Book**. Review usually takes up to 72 hours.

## Before you publish — quick checks

- Search Amazon for "Color Me Happy coloring book". If the exact title is already common, consider adding a word, e.g. **Color Me Happy! Animal Adventures**. The cover and interior are generated from `build_kdp.py` (`TITLE` at the top), so the title is easy to change.
- Order an **author proof copy** (Bookshelf › ⋯ › Request proof copies) to check line thickness and colors in your hands before customers do.
- KDP's free **A+ Content** (Marketing › A+ Content) lets you add page previews under the listing. The PNGs in `../output/png-300dpi/` work well for this.

## Rebuilding

```bash
python3 build.py            # coloring pages -> svg/, PNGs, Letter & A4 PDFs
python3 kdp/build_kdp.py    # KDP interior + cover (spine width is recalculated from the page count)
```
