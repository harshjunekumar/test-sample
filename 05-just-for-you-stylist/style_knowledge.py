"""Styling knowledge for the "Just for you" chatbot.

Outfits, accessories, colour palettes and tips are written by hand. The TRENDS
section summarises 2026 fashion trend articles found on Google (sources listed),
researched in October 2026. To refresh the bot, update this file.
"""

GENDERS = {"woman": "Woman", "man": "Man", "neutral": "Prefer not to say"}
AGE_BANDS = ["Under 18", "18-24", "25-34", "35-44", "45-54", "55+"]
WEAR = {"western": "Western", "indo": "Indo-western", "traditional": "Traditional", "mix": "A mix of everything"}
VIBES = {"comfortable": "Comfortable", "classy": "Classy", "fashionable": "Fashionable", "statement": "Statement"}
OCCASIONS = {"office": "Office", "casual": "Casual weekend", "party": "Party / night out",
             "festive": "Festive / puja", "wedding": "Wedding"}

# ---- Persona naming ----------------------------------------------------------
VIBE_PERSONA = {
    "comfortable": ("Effortless", "You love clothes that feel as good as they look: easy fits, soft fabrics, zero fuss."),
    "classy": ("Timeless", "You prefer clean lines, quality fabrics and pieces that never go out of style."),
    "fashionable": ("Trend-Forward", "You enjoy trying what's new and keeping your look fresh every season."),
    "statement": ("Bold", "You dress to be noticed: strong colours, standout silhouettes and confident details."),
}
WEAR_PERSONA = {
    "western": ("City Dresser", "Western silhouettes are your everyday go-to."),
    "indo": ("Fusion Lover", "You mix Indian craft with modern cuts."),
    "traditional": ("Heritage Lover", "You love the richness of Indian traditional wear."),
    "mix": ("Style Shapeshifter", "You switch between western, fusion and traditional depending on the day."),
}

# ---- Colour palettes ---------------------------------------------------------
# name -> list of (colour name, hex)
PALETTES = {
    "Neutrals & whites": [("cloud white", "#F0EEE9"), ("beige", "#D9C7A7"), ("taupe", "#8B7D6B"), ("navy", "#1F2A44")],
    "Pastels": [("powder blue", "#B8D4E8"), ("mint green", "#BDE5D1"), ("blush pink", "#F4C6C6"), ("lavender", "#CDBFE3")],
    "Earthy tones": [("sage green", "#A3B18A"), ("rust", "#B5562C"), ("mocha", "#6F4E37"), ("olive", "#6B6B3A")],
    "Jewel tones": [("emerald", "#0F7B5F"), ("ruby red", "#9B111E"), ("deep teal", "#0E5E6F"), ("sapphire", "#1F3F99")],
    "Bright & bold": [("tomato red", "#E5412D"), ("cobalt blue", "#1B4FD6"), ("fuchsia", "#D6247F"), ("sunshine yellow", "#F6C343")],
    "Black & monochrome": [("black", "#111111"), ("charcoal", "#3A3A3A"), ("silver grey", "#B8B8B8"), ("white", "#FFFFFF")],
    "Surprise me (2026 trend colours)": [("transformative teal", "#1F6F78"), ("cloud dancer white", "#F0EEE9"),
                                         ("tomato red", "#E5412D"), ("cobalt blue", "#1B4FD6")],
}
PALETTE_TIPS = {
    "Neutrals & whites": "Mix textures (linen, knit, silk) so an all-neutral look never feels flat.",
    "Pastels": "Pair pastels with white or beige for a fresh look; add one darker accessory for definition.",
    "Earthy tones": "Earthy shades look richest in natural fabrics. Gold-toned accessories warm them up further.",
    "Jewel tones": "Let one jewel tone lead and keep the rest neutral, or pair two (emerald + ruby) for festive drama.",
    "Bright & bold": "Wear one bright piece with neutrals, or go colour-block with two brights for full impact.",
    "Black & monochrome": "Play with silhouettes and textures; a metallic or a single colour accessory lifts the look.",
    "Surprise me (2026 trend colours)": "Cloud Dancer white is Pantone's 2026 colour; pair it with teal or a pop of tomato red.",
}

# ---- Outfits: OUTFITS[gender][wear][vibe] = [(hero piece, how to style it), ...] ----
OUTFITS = {
    "woman": {
        "western": {
            "comfortable": [("relaxed linen co-ord set", "with white sneakers and a canvas tote"),
                            ("wide-leg trousers and oversized shirt", "with flat mules"),
                            ("knit midi dress", "with a denim jacket and slip-on sneakers")],
            "classy": [("tailored blazer and straight trousers", "with a silk camisole and pointed flats"),
                       ("wrap midi dress", "with block heels and a structured bag"),
                       ("crisp white shirt and pleated midi skirt", "with loafers and pearl studs")],
            "fashionable": [("structured co-ord set", "with chunky loafers"),
                            ("barrel-leg jeans and cropped cardigan", "with kitten heels"),
                            ("bold floral print midi dress", "with strappy sandals")],
            "statement": [("colour-block pantsuit", "with a sleek bun and metallic heels"),
                          ("sequinned slip dress", "with a minaudiere clutch"),
                          ("animal-print shirt dress", "with knee-high boots")],
        },
        "indo": {
            "comfortable": [("cotton kurta with straight jeans", "with kolhapuri flats"),
                            ("printed kaftan with palazzo pants", "with juttis"),
                            ("pastel kurta co-ord set", "with oxidised silver jhumkas")],
            "classy": [("straight kurta with cigarette pants", "and a printed silk stole"),
                       ("cape-style kurta set", "with embroidered juttis"),
                       ("saree gown", "with a slim belt and potli bag")],
            "fashionable": [("crop top with dhoti pants", "and an organza jacket"),
                            ("asymmetric kurta with flared pants", "and statement earrings"),
                            ("fusion jumpsuit with ethnic print", "with block heels")],
            "statement": [("organza cape set with embroidery", "and a metallic potli"),
                          ("embroidered crop top with palazzo", "and chandbalis"),
                          ("ruffled slit saree", "with a corset blouse")],
        },
        "traditional": {
            "comfortable": [("cotton anarkali kurta set", "with juttis"),
                            ("handloom cotton saree", "with a simple blouse and kolhapuris"),
                            ("chikankari salwar suit", "with a mulmul dupatta")],
            "classy": [("silk saree with contrast border", "and temple jewellery"),
                       ("tailored silk salwar suit", "with pearl earrings"),
                       ("Banarasi dupatta with plain kurta set", "and gold studs")],
            "fashionable": [("pastel lehenga with tone-on-tone embroidery", "and a sheer dupatta"),
                            ("sharara set with short kurta", "and statement jhumkas"),
                            ("pre-draped saree", "with a structured blouse")],
            "statement": [("jewel-tone velvet lehenga", "with a layered necklace"),
                          ("Kanjeevaram silk saree", "with a bold temple choker"),
                          ("mirror-work ghagra choli", "with oxidised jewellery")],
        },
    },
    "man": {
        "western": {
            "comfortable": [("relaxed-fit linen shirt and chinos", "with white sneakers"),
                            ("crew-neck tee and straight jeans", "with an overshirt"),
                            ("knit polo and drawstring trousers", "with loafers")],
            "classy": [("unstructured blazer and tailored trousers", "with leather loafers"),
                       ("crisp oxford shirt and dark chinos", "with a leather watch"),
                       ("merino knit and pleated trousers", "with suede derbies")],
            "fashionable": [("boxy overshirt and wide-leg trousers", "with chunky sneakers"),
                            ("camp-collar printed shirt", "with relaxed denim"),
                            ("knitted co-ord set", "with minimal sneakers")],
            "statement": [("bold colour suit", "with a monochrome tee"),
                          ("printed silk shirt", "with leather trousers"),
                          ("double-breasted blazer in a jewel tone", "with tapered trousers")],
        },
        "indo": {
            "comfortable": [("short linen kurta with chinos", "and kolhapuris"),
                            ("cotton kurta with straight jeans", "and loafers"),
                            ("Nehru jacket over a tee", "with relaxed trousers")],
            "classy": [("bandhgala jacket with straight trousers", "and leather mojaris"),
                       ("Nehru jacket over a white shirt", "with tailored trousers"),
                       ("structured straight-cut kurta", "with slim trousers and a silk pocket square")],
            "fashionable": [("asymmetric hem kurta", "with tapered trousers"),
                            ("bandhgala with dark jeans", "and minimal sneakers"),
                            ("printed indo-western jacket set", "with loafers")],
            "statement": [("embroidered sherwani-style jacket with straight trousers", "and a brooch"),
                          ("silk kurta with leather trousers", "and statement mojaris"),
                          ("velvet bandhgala in a jewel tone", "with a layered chain")],
        },
        "traditional": {
            "comfortable": [("cotton kurta pyjama set", "with kolhapuris"),
                            ("linen kurta with churidar", "and juttis"),
                            ("khadi kurta set", "with a cotton stole")],
            "classy": [("silk kurta with Nehru jacket", "and mojaris"),
                       ("ivory bandhgala set", "with a pocket square"),
                       ("dhoti kurta in silk", "with a gold-border angavastram")],
            "fashionable": [("pastel kurta with subtle zari work", "and juttis"),
                            ("printed kurta with straight pants", "and a layered stole"),
                            ("short sherwani set", "with mojaris")],
            "statement": [("zardozi-embroidered sherwani", "with a safa and kalgi"),
                          ("velvet Nehru jacket set", "with a brooch"),
                          ("brocade kurta in a jewel tone", "with embroidered juttis")],
        },
    },
    "neutral": {
        "western": {
            "comfortable": [("oversized shirt and wide-leg trousers", "with sneakers"),
                            ("relaxed hoodie and cargo pants", "with high-tops"),
                            ("linen co-ord set", "with sliders")],
            "classy": [("boxy blazer and straight trousers", "with loafers"),
                       ("fine-knit sweater and tailored pants", "with a minimal watch"),
                       ("trench coat over a monochrome outfit", "with leather sneakers")],
            "fashionable": [("utility jacket and barrel-leg jeans", "with chunky sneakers"),
                            ("printed camp-collar shirt", "with relaxed trousers"),
                            ("cropped knit vest over a shirt", "with wide trousers")],
            "statement": [("colour-block co-ord set", "with platform boots"),
                          ("metallic bomber jacket", "with black jeans"),
                          ("printed suit", "with a tank top")],
        },
        "indo": {
            "comfortable": [("unisex cotton kurta with straight pants", "and kolhapuris"),
                            ("Nehru jacket over a tee", "with wide trousers"),
                            ("block-print shirt with dhoti pants", "and sliders")],
            "classy": [("bandhgala jacket with tailored trousers", "and loafers"),
                       ("straight kurta with a silk stole", "and minimal jewellery"),
                       ("linen jacket set with ethnic buttons", "and mojaris")],
            "fashionable": [("asymmetric kurta with tapered pants", "and sneakers"),
                            ("organza overlay jacket on a monochrome set", "with loafers"),
                            ("ikat print co-ord set", "with chunky sandals")],
            "statement": [("embroidered cape jacket over a co-ord", "with a statement brooch"),
                          ("velvet bandhgala in a jewel tone", "with layered chains"),
                          ("mirror-work jacket", "with black trousers")],
        },
        "traditional": {
            "comfortable": [("handloom cotton kurta set", "with kolhapuris"),
                            ("khadi kurta with straight pants", "and a cotton stole"),
                            ("chikankari kurta", "with relaxed pants")],
            "classy": [("silk kurta with Nehru jacket", "and mojaris"),
                       ("handwoven silk kurta set", "with a Banarasi stole"),
                       ("ivory kurta with zari border", "and juttis")],
            "fashionable": [("pastel kurta with tone-on-tone embroidery", "and juttis"),
                            ("printed kurta with sharara-style pants", "and a stole"),
                            ("short kurta with dhoti pants", "and mojaris")],
            "statement": [("brocade kurta in a jewel tone", "with embroidered juttis"),
                          ("mirror-work kurta set", "with oxidised jewellery"),
                          ("velvet kurta with a zari stole", "and a statement brooch")],
        },
    },
}

# ---- Occasion outfits: OCCASION_OUTFITS[gender][occasion] = {western, indo, traditional} ----
OCCASION_OUTFITS = {
    "woman": {
        "office": {"western": ("tailored trouser suit", "with a silk shell and loafers"),
                   "indo": ("straight kurta with cigarette pants", "and a structured tote"),
                   "traditional": ("cotton silk saree", "with a tailored blouse and minimal studs")},
        "casual": {"western": ("denim and breton-stripe tee", "with ballet flats"),
                   "indo": ("short kurti with jeans", "and kolhapuris"),
                   "traditional": ("cotton salwar suit", "with juttis")},
        "party": {"western": ("satin slip dress", "with strappy heels and a minaudiere"),
                  "indo": ("sequinned crop top with palazzo", "and statement earrings"),
                  "traditional": ("georgette saree with sequins", "and a sleek clutch")},
        "festive": {"western": ("jewel-tone co-ord set", "with gold jewellery"),
                    "indo": ("cape kurta set", "with jhumkas"),
                    "traditional": ("silk anarkali", "with a Banarasi dupatta")},
        "wedding": {"western": ("embellished gown", "with a statement necklace"),
                    "indo": ("organza cape lehenga", "with chandbalis"),
                    "traditional": ("Banarasi or Kanjeevaram silk saree", "with temple jewellery")},
    },
    "man": {
        "office": {"western": ("navy blazer with chinos", "and leather loafers"),
                   "indo": ("Nehru jacket over a formal shirt", "with trousers"),
                   "traditional": ("structured cotton kurta", "with tailored trousers")},
        "casual": {"western": ("polo tee with shorts or chinos", "and white sneakers"),
                   "indo": ("short linen kurta with jeans", "and sliders"),
                   "traditional": ("cotton kurta pyjama", "with kolhapuris")},
        "party": {"western": ("black shirt with a velvet blazer", "and chelsea boots"),
                  "indo": ("bandhgala with dark jeans", "and loafers"),
                  "traditional": ("silk kurta with a printed Nehru jacket", "and mojaris")},
        "festive": {"western": ("linen shirt in a jewel tone", "with beige trousers"),
                    "indo": ("asymmetric kurta set", "with mojaris"),
                    "traditional": ("silk kurta pyjama", "with a Nehru jacket")},
        "wedding": {"western": ("tuxedo or tailored suit", "with a pocket square"),
                    "indo": ("embroidered sherwani with straight trousers", "and a brooch"),
                    "traditional": ("zardozi sherwani", "with a safa and mojaris")},
    },
    "neutral": {
        "office": {"western": ("boxy blazer with tailored trousers", "and loafers"),
                   "indo": ("straight kurta with trousers", "and a structured bag"),
                   "traditional": ("handloom kurta set", "with minimal jewellery")},
        "casual": {"western": ("oversized tee with relaxed jeans", "and sneakers"),
                   "indo": ("block-print shirt with dhoti pants", "and sliders"),
                   "traditional": ("cotton kurta with straight pants", "and kolhapuris")},
        "party": {"western": ("satin shirt with wide-leg trousers", "and platform shoes"),
                  "indo": ("velvet bandhgala with black trousers", "and a chain"),
                  "traditional": ("silk kurta with a zari stole", "and mojaris")},
        "festive": {"western": ("jewel-tone co-ord set", "with metallic accessories"),
                    "indo": ("Nehru jacket over a silk kurta", "with loafers"),
                    "traditional": ("brocade kurta set", "with juttis")},
        "wedding": {"western": ("tailored suit in a rich colour", "with a brooch"),
                    "indo": ("embroidered long jacket over a co-ord", "with mojaris"),
                    "traditional": ("silk kurta with an embroidered stole", "and juttis")},
    },
}

# ---- Accessories: ACCESSORIES[gender][vibe] -----------------------------------
ACCESSORIES = {
    "woman": {
        "comfortable": {"Footwear": "white sneakers or kolhapuri flats", "Bag": "canvas tote",
                        "Jewellery": "small hoops or oxidised silver studs", "Extra": "cotton stole or bucket hat"},
        "classy": {"Footwear": "pointed flats or block heels", "Bag": "structured leather tote",
                   "Jewellery": "pearl studs and a fine gold chain", "Extra": "classic leather-strap watch"},
        "fashionable": {"Footwear": "kitten heels or chunky loafers", "Bag": "woven shoulder bag",
                        "Jewellery": "layered necklaces and stacked rings", "Extra": "statement sunglasses"},
        "statement": {"Footwear": "metallic heels or embellished juttis", "Bag": "minaudiere clutch or potli",
                      "Jewellery": "chunky beaded necklace or chandbalis", "Extra": "statement brooch"},
    },
    "man": {
        "comfortable": {"Footwear": "white sneakers or kolhapuris", "Bag": "canvas backpack",
                        "Jewellery": "simple bracelet", "Extra": "cotton cap"},
        "classy": {"Footwear": "leather loafers or mojaris", "Bag": "leather messenger bag",
                   "Jewellery": "signet ring", "Extra": "minimal leather-strap watch"},
        "fashionable": {"Footwear": "chunky sneakers", "Bag": "sling bag",
                        "Jewellery": "silver chain", "Extra": "tinted sunglasses"},
        "statement": {"Footwear": "embroidered mojaris or chelsea boots", "Bag": "textured leather pouch",
                      "Jewellery": "layered chains and a bold ring", "Extra": "lapel brooch or pocket square"},
    },
    "neutral": {
        "comfortable": {"Footwear": "sneakers or sliders", "Bag": "canvas tote", "Jewellery": "simple silver ring",
                        "Extra": "bucket hat"},
        "classy": {"Footwear": "leather loafers", "Bag": "structured crossbody", "Jewellery": "fine chain",
                   "Extra": "minimal watch"},
        "fashionable": {"Footwear": "chunky sneakers", "Bag": "sling bag", "Jewellery": "layered silver chains",
                        "Extra": "statement sunglasses"},
        "statement": {"Footwear": "platform boots", "Bag": "metallic pouch", "Jewellery": "chunky beaded necklace",
                      "Extra": "brooch"},
    },
}

# ---- Age-band tips -----------------------------------------------------------
AGE_TIPS = {
    "Under 18": ["Keep it fun and comfortable: co-ords, sneakers and easy layers work everywhere.",
                 "Try trends with affordable pieces first and see what you really love."],
    "18-24": ["This is the best time to experiment: try one new trend each season.",
              "Build a few versatile basics (white tee, good jeans, a kurta) to mix with trendy pieces."],
    "25-34": ["Start building a capsule wardrobe: fewer, better pieces that mix and match.",
              "Invest in one great blazer or bandhgala; it works for office and occasions."],
    "35-44": ["Focus on fit and fabric: tailoring makes simple outfits look expensive.",
              "Mix classic pieces with one trend element to stay current without effort."],
    "45-54": ["Choose rich fabrics like silk, linen and fine cotton, which drape well and feel great.",
              "A few quality accessories (watch, bag, jewellery) refresh outfits you already own."],
    "55+": ["Comfort and elegance go together: soft structure, breathable fabrics, easy fastenings.",
            "Colour near the face (a stole, scarf or kurta) brightens the whole look."],
}

# ---- 2026 trends found on Google (with sources) ----------------------------------
TRENDS = {
    "colour": [("Pantone's Colour of the Year 2026 is 'Cloud Dancer', a soft off-white; teal, tomato red and cobalt blue are big on runways.",
                "https://time.com/7338176/pantone-color-of-the-year-2026/"),
               ("Jewel tones (ruby, teal, burgundy, emerald) and soft-glam pastels lead Indian fashion this year.",
                "https://www.likeadiva.com/editorial/latest-trends/latest-fashion-trends-2026-the-hottest-indian-fashion-picks-for-women")],
    "woman": [("Structured co-ord sets and bold prints (florals, animal print) are redefining western wear in India.",
               "https://isufashion.com/blogs/news/top-10-western-fashion-trends-for-indian-women-in-2026"),
              ("Organza capes, crop top + palazzo sets and slit sarees with ruffled hems lead indo-western and festive wear.",
               "https://sareesbazaar.com/blogs/news/indo-western-festive-fashion-trends"),
              ("Pastel co-ords, fluid sarees and tone-on-tone embroidery are everyday ethnic favourites.",
               "https://www.samyakk.com/blog/ethnic-wear-trends-women-2026-top-styles-designs-watch/")],
    "man": [("Kurtas are sharper and more structured, in pastels like ivory, mint and powder blue with subtle zari.",
             "https://bhasinbrothers.com/blogs/bb/top-10-mens-ethnic-wear-trends-2026-where-heritage-meets-modernity"),
            ("Indo-western is cleaner: asymmetric hems, sherwanis with straight trousers instead of churidars.",
             "https://www.azafashions.com/blog/best-indo-western-wedding-outfits-to-wear-in-2026/"),
            ("Breathable linen, cotton and silk blends dominate as comfort becomes a priority.",
             "https://ethnixbyraymond.in/blogs/weddings/top-10-mens-ethnic-wear-trends-2026-the-essential-modern-mens-style-guide")],
    "accessories": [("Jewellery is moving past minimalism: layered necklaces, pearls, chunky beads and statement earrings.",
                     "https://fitinline.com/article/read/fashion-accessories-trends-2026/"),
                    ("Structured bags and small evening clutches (minaudieres) are back; kitten heels and cap-toe shoes trend.",
                     "https://www.wmagazine.com/fashion/spring-2026-accessory-trends-shoes-bags-jewelry-sunglasses")],
}
