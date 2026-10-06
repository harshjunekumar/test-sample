"""Tests for the "Just for you" stylist. Run: python test_stylist.py"""
import itertools

import style_knowledge as K
from stylist import Stylist, parse

# Typed answers are understood
assert parse("gender", "female, 28") == "woman" and parse("age", "female, 28") == "25-34"
assert parse("gender", "I am a guy") == "man" and parse("gender", "I'm 30") is None
assert parse("wear", "indo western") == "indo" and parse("wear", "mostly ethnic") == "traditional"
assert parse("vibe", "comfy") == "comfortable" and parse("vibe", "something bold") == "statement"
assert parse("colour", "I love pastels") == "Pastels" and parse("colour", "not sure") .startswith("Surprise")
assert parse("occasion", "my friend's sangeet") == "wedding"

# One message can answer gender and age together; the flow then asks the next question
b = Stylist()
assert "wear" in b.reply("female 28")["text"]
assert b.answers == {"gender": "woman", "age": "25-34"}

# Unclear answers get a polite retry, not a crash
assert "didn't catch" in Stylist().reply("banana")["text"]

# Every combination of answers produces a full recommendation and every occasion look works
for g, age, wear, vibe, colour in itertools.product(K.GENDERS.values(), K.AGE_BANDS, K.WEAR.values(),
                                                     K.VIBES.values(), K.PALETTES):
    b = Stylist()
    for answer in (g, age, wear, vibe, colour):
        r = b.reply(answer)
    assert "Your style persona" in r["text"] and len(r["palette"]) == 4, (g, age, wear, vibe, colour)
    assert r["text"].count("Shop on Google") == 3 and r["text"].count("Complete the look") == 3
    assert "{" not in r["text"], "an accessory placeholder was not filled in"
    for occ in K.OCCASIONS.values():
        assert "look, just for you" in b.reply(occ)["text"]

# Complete looks have the right accessories for each gender
REQUIRED = {"Woman": ["Purse", "Earrings", "Pendant / necklace", "Sunglasses", "Footwear", "Watch / bangles"],
            "Man": ["Watch", "Sunglasses", "Footwear", "Finishing touch"],
            "Prefer not to say": ["Bag", "Jewellery", "Watch", "Sunglasses", "Footwear"]}
for g, slots in REQUIRED.items():
    b = Stylist()
    for answer in (g, "25-34", "A mix of everything", "Classy", "Pastels"):
        r = b.reply(answer)
    for slot in slots:
        assert r["text"].count(f"**{slot}:**") == 3, (g, slot)

# Accessories follow the answers: metal from the colour, jewellery style from the wear type
b = Stylist()
for answer in ("Woman", "25-34", "Traditional", "Classy", "Black & monochrome"):
    r = b.reply(answer)
assert "silver" in r["text"] and "jhumkas" in r["text"]
b = Stylist()
for answer in ("Man", "25-34", "Indo-western", "Comfortable", "Earthy tones"):
    b.reply(answer)
assert "backpack" not in b.reply("Wedding")["text"]          # dressed up for the occasion

# Follow-ups change the result, and Start over resets
b = Stylist()
for answer in ("Man", "25-34", "Western", "Classy", "Neutrals & whites"):
    b.reply(answer)
assert "Updated your colour" in b.reply("show me pastels")["text"]
b.reply("Start over")
assert b.answers == {} and b.step == "gender"
print("All stylist tests passed")
