"""Conversation engine for the "Just for you" styling chatbot.

Asks four questions (gender & age, what you wear, style vibe, colour), then
builds a style persona with outfits, accessories, a colour palette, tips,
2026 trends and Google links. Free: no AI model or API key.
Answers can be given by tapping buttons or by typing (e.g. "female, 28").
"""
import re
from urllib.parse import quote_plus

import style_knowledge as K

STEPS = ["gender", "age", "wear", "vibe", "colour"]
QUESTIONS = {
    "gender": "First, **what is your gender and age?** Pick your gender below (or type e.g. *female, 28*).",
    "age": "And **your age?**",
    "wear": "**What do you like to wear most often?**",
    "vibe": "**Do you like comfortable, classy, fashionable or statement clothing?**",
    "colour": "Last one: **what is your colour preference?**",
}
GENDER_WORD = {"woman": "women", "man": "men", "neutral": "unisex"}

# keyword -> value, checked in order (so "female" is matched before "male")
KEYWORDS = {
    "gender": [(r"\b(woman|women|female|girl|lady)\b|^f\b", "woman"), (r"\b(man|men|male|boy|guy)\b|^m\b", "man"),
               (r"(non.?binary|prefer not|other|neutral|rather not)", "neutral")],
    "wear": [(r"(indo|fusion)", "indo"), (r"(traditional|ethnic|desi)", "traditional"), (r"western", "western"),
             (r"\b(mix|all|everything|both)\b", "mix")],
    "vibe": [(r"(comfort|comfy|relaxed|easy)", "comfortable"), (r"(classy|elegant|classic|sophisticated)", "classy"),
             (r"(fashionable|trend|stylish)", "fashionable"), (r"(statement|bold|stand ?out|loud)", "statement")],
    "colour": [(r"(surprise|not sure|any|trend)", "Surprise me (2026 trend colours)"),
               (r"(pastel|light|soft)", "Pastels"),
               (r"(neutral|white|beige|cream|nude)", "Neutrals & whites"),
               (r"(earth|brown|olive|rust|sage|mocha)", "Earthy tones"),
               (r"(jewel|emerald|ruby|teal|wine|maroon|sapphire)", "Jewel tones"),
               (r"(black|monochrome|grey|gray|dark)", "Black & monochrome"),
               (r"(bright|bold|vibrant|red|yellow|pink|orange|colou?rful|cobalt)", "Bright & bold")],
    "occasion": [(r"(office|work|meeting|interview)", "office"), (r"(casual|weekend|daily|everyday|brunch)", "casual"),
                 (r"(party|night|club|date|dinner)", "party"), (r"(festive|festival|diwali|puja|eid|holi|navratri)", "festive"),
                 (r"(wedding|sangeet|mehendi|haldi|reception|shaadi)", "wedding")],
}
LABELS = {"gender": K.GENDERS, "wear": K.WEAR, "vibe": K.VIBES,
          "colour": {p: p for p in K.PALETTES}, "occasion": K.OCCASIONS}


def shop_link(query: str) -> str:
    return "https://www.google.com/search?tbm=shop&q=" + quote_plus(query)


def looks_link(query: str) -> str:
    return "https://www.google.com/search?tbm=isch&q=" + quote_plus(query + " outfit")


ACCESSORY_WORDS = re.compile(
    r"(sneaker|flat|heel|jutti|kolhapuri|mojari|loafer|boot|sandal|mule|derb|slider|high-top|bag|tote|clutch|"
    r"potli|minaudiere|jhumka|earring|chandbali|stud|hoop|chain|necklace|choker|jewel|watch|brooch|bracelet|"
    r"pocket square|kalgi|shoe|accessor)")
# Occasions shift the accessory style: e.g. a "comfortable" dresser gets classy accessories for a wedding
OCCASION_VIBE = {"wedding": {"comfortable": "classy", "fashionable": "statement"},
                 "festive": {"comfortable": "classy"},
                 "party": {"comfortable": "fashionable", "classy": "fashionable"},
                 "office": {"statement": "classy", "fashionable": "classy"}}
ICONS = {"Footwear": "👟", "Purse": "👜", "Bag": "👜", "Earrings": "💎", "Pendant / necklace": "📿",
         "Sunglasses": "🕶️", "Watch / bangles": "⌚", "Watch": "⌚", "Finishing touch": "✨", "Jewellery": "💍"}


def clean_styling(styling: str) -> str:
    """Drop accessory mentions (shoes, bags, jewellery) from an outfit's styling note, since the
    complete look lists accessories separately. 'with a denim jacket and slip-on sneakers' -> 'with a denim jacket'."""
    parts = re.split(r",? and |, ", re.sub(r"^(with|and) ", "", styling))
    keep = [p for p in parts if not ACCESSORY_WORDS.search(p)]
    return ("with " + " and ".join(keep)) if keep else ""


def age_band(age: int) -> str:
    for limit, band in [(17, "Under 18"), (24, "18-24"), (34, "25-34"), (44, "35-44"), (54, "45-54")]:
        if age <= limit:
            return band
    return "55+"


def parse(field: str, text: str):
    """Find a value for one field in free text (or an exact button label)."""
    t = text.lower().strip()
    if field == "age":
        if text in K.AGE_BANDS:
            return text
        m = re.search(r"\b(\d{1,2})\b", t)
        return age_band(int(m.group(1))) if m and 5 <= int(m.group(1)) <= 99 else None
    for value, label in LABELS.get(field, {}).items():   # exact button label
        if t == label.lower():
            return value
    for pattern, value in KEYWORDS[field]:
        if re.search(pattern, t):
            return value
    return None


class Stylist:
    def __init__(self):
        self.answers = {}

    # ---- conversation state --------------------------------------------------
    @property
    def step(self):
        return next((s for s in STEPS if s not in self.answers), "done")

    def options(self) -> list[str]:
        """Quick-reply buttons for the current step."""
        if self.step == "age":
            return K.AGE_BANDS
        if self.step == "done":
            return list(K.OCCASIONS.values()) + ["Start over"]
        return list(LABELS[self.step].values())

    def greeting(self) -> dict:
        return {"text": "Hi, I'm your personal stylist ✨ Answer 4 quick questions and I'll put together "
                        "looks picked **just for you**.\n\n" + QUESTIONS["gender"]}

    # ---- main entry point ----------------------------------------------------
    def reply(self, text: str) -> dict:
        """Take the customer's message, return the bot's reply: {"text": markdown, "palette": [...]}."""
        t = text.lower().strip()
        if re.search(r"(start over|restart|reset|again)", t):
            self.answers = {}
            return {"text": "Let's start fresh! " + QUESTIONS["gender"]}

        if self.step == "done":
            return self._follow_up(text)

        step = self.step
        value = parse(step, text)
        if value is None:
            return {"text": "Sorry, I didn't catch that. Please tap an option below or type it in.\n\n" + QUESTIONS[step]}
        self.answers[step] = value
        if step == "gender" and "age" not in self.answers:      # "female, 28" answers both
            age = parse("age", text)
            if age:
                self.answers["age"] = age
        return self.recommend() if self.step == "done" else {"text": QUESTIONS[self.step]}

    def _follow_up(self, text: str) -> dict:
        occasion = parse("occasion", text)
        if occasion:
            return self.occasion_look(occasion)
        for field in ["colour", "vibe", "wear"]:          # e.g. "show me pastels" or "something classy"
            value = parse(field, text)
            if value and value != self.answers[field]:
                self.answers[field] = value
                return self.recommend(intro=f"Updated your {field} to **{LABELS[field][value]}**. ")
        return {"text": "I can show looks for an occasion (office, casual, party, festive, wedding), or change your "
                        "colour or style, e.g. *show me pastels* or *something classy*. Or tap **Start over**."}

    # ---- recommendations -----------------------------------------------------
    def _colour_for(self, i: int) -> str:
        return K.PALETTES[self.answers["colour"]][i % 4][0]

    def _outfits(self) -> list:
        g, wear, vibe = self.answers["gender"], self.answers["wear"], self.answers["vibe"]
        if wear == "mix":
            return [K.OUTFITS[g][w][vibe][0] for w in ["western", "indo", "traditional"]]
        return K.OUTFITS[g][wear][vibe]

    def _item_line(self, colour: str, hero: str, styling: str) -> str:
        # Put the customer's colour into generic phrases like "in a jewel tone" / "bold colour suit"
        for generic in ["in a jewel tone", "jewel-tone", "bold colour"]:
            if generic in hero:
                hero = hero.replace(generic, f"in {colour}" if generic.startswith("in ") else colour)
                colour = ""
        has_colour = not colour or re.search(r"\b(black|white|ivory|navy|dark|pastel|metallic|animal|floral)", hero)
        title = f"{hero[0].upper()}{hero[1:]}"
        if colour:
            title += f", plus a touch of {colour}" if has_colour else f" in {colour}"
        q = f"{'' if has_colour else colour + ' '}{hero.split(' or ')[0]} {GENDER_WORD[self.answers['gender']]}"
        styling = clean_styling(styling)
        return (f"**{title}**{' ' + styling if styling else ''}  \n"
                f"[🛍 Shop on Google]({shop_link(q)}) · [🖼 See looks]({looks_link(q)})  ")

    def persona(self) -> tuple[str, str]:
        adj, vibe_desc = K.VIBE_PERSONA[self.answers["vibe"]]
        noun, wear_desc = K.WEAR_PERSONA[self.answers["wear"]]
        return f"The {adj} {noun}", f"{vibe_desc} {wear_desc}"

    def _trends(self) -> list:
        g, wear = self.answers["gender"], self.answers["wear"]
        pick = {"woman": {"western": 0, "indo": 1, "traditional": 2, "mix": 1},
                "man": {"western": 2, "indo": 1, "traditional": 0, "mix": 1}}
        picks = [K.TRENDS["colour"][0 if self.answers["colour"].startswith("Surprise") else 1]]
        if g in pick:
            picks.append(K.TRENDS[g][pick[g][wear]])
        picks.append(K.TRENDS["accessories"][0 if self.answers["vibe"] in ("fashionable", "statement") else 1])
        return picks

    def _family(self, i: int) -> str:
        wear = self.answers["wear"]
        return ["western", "indo", "traditional"][i] if wear == "mix" else wear

    def complete_look(self, i: int, family: str, occasion: str = None) -> list[tuple[str, str, str]]:
        """Accessories for outfit number i: [(icon, slot, item)], matched to gender, wear, vibe and colour.
        For an occasion, accessories are dressed up (wedding, festive, party) or toned down (office)."""
        a = self.answers
        g, vibe = a["gender"], OCCASION_VIBE.get(occasion, {}).get(a["vibe"], a["vibe"])
        fill = {"metal": K.METAL[a["colour"]], "accent": K.PALETTES[a["colour"]][(i + 2) % 4][0]}

        def pick(options: str) -> str:
            choices = options.split("|")
            return choices[i % len(choices)].format(**fill)

        if g == "woman":
            slots = [(slot, by[family][vibe] if slot != "Sunglasses" else by[vibe]) for slot, by in K.LOOK_WOMAN.items()]
        elif g == "man":
            slots = [(slot, by[family][vibe] if family in by else by[vibe]) for slot, by in K.LOOK_MAN.items()]
        else:
            slots = [("Footwear", K.LOOK_MAN["Footwear"][family][vibe]), ("Bag", K.LOOK_NEUTRAL["Bag"][vibe]),
                     ("Jewellery", K.LOOK_NEUTRAL["Jewellery"][vibe]), ("Watch", K.LOOK_MAN["Watch"][vibe]),
                     ("Sunglasses", K.LOOK_MAN["Sunglasses"][vibe])]
        return [(ICONS[slot], slot, pick(options)) for slot, options in slots]

    def _look_block(self, i: int, family: str, occasion: str = None) -> str:
        gw = GENDER_WORD[self.answers["gender"]]
        lines = [f"   - {icon} **{slot}:** [{item}]({shop_link(item + ' ' + gw)})"
                 for icon, slot, item in self.complete_look(i, family, occasion)]
        return "   *Complete the look:*\n" + "\n".join(lines)

    def recommend(self, intro: str = "") -> dict:
        a = self.answers
        name, desc = self.persona()
        looks = "\n".join(f"{i}. {self._item_line(self._colour_for(i - 1), hero, styling)}\n{self._look_block(i - 1, self._family(i - 1))}\n"
                          for i, (hero, styling) in enumerate(self._outfits(), 1))
        tips = "\n".join(f"- {t}" for t in K.AGE_TIPS[a["age"]])
        trends = "\n".join(f"- {t} ([source]({url}))" for t, url in self._trends())
        text = (f"{intro}✨ **Your style persona: {name}**  \n*{desc}*\n\n"
                f"#### 👗 Complete looks picked just for you\n{looks}\n"
                f"#### 🎨 Your colour palette: {a['colour']}\n{K.PALETTE_TIPS[a['colour']]} "
                f"Your accessories are in **{K.METAL[a['colour']]}** tones to match.\n\n"
                f"#### 💡 Tips for your age group ({a['age']})\n{tips}\n\n"
                f"#### 🔥 Trending in 2026 (from the web)\n{trends}\n\n"
                "Want a look for a specific occasion? Tap one below, or type something like *show me pastels*.")
        return {"text": text, "palette": K.PALETTES[a["colour"]]}

    def occasion_look(self, occasion: str) -> dict:
        a = self.answers
        wear = a["wear"] if a["wear"] != "mix" else ("traditional" if occasion in ("festive", "wedding") else "western")
        main = K.OCCASION_OUTFITS[a["gender"]][occasion][wear]
        alt_wear = "indo" if wear != "indo" else ("traditional" if occasion in ("festive", "wedding") else "western")
        alt = K.OCCASION_OUTFITS[a["gender"]][occasion][alt_wear]
        text = (f"#### {K.OCCASIONS[occasion]} look, just for you\n"
                f"1. {self._item_line(self._colour_for(0), *main)}\n{self._look_block(0, wear, occasion)}\n\n"
                f"2. Or try {K.WEAR[alt_wear].lower()}: {self._item_line(self._colour_for(1), *alt)}\n"
                f"{self._look_block(1, alt_wear, occasion)}\n\n"
                "Pick another occasion, or tap **Start over**.")
        return {"text": text}


if __name__ == "__main__":
    bot = Stylist()
    print(bot.greeting()["text"].replace("**", ""))
    while True:
        print("Options:", " | ".join(bot.options()))
        try:
            msg = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if msg.lower() in {"quit", "exit"}:
            break
        print("\n" + bot.reply(msg)["text"] + "\n")
