"""Tests for the free rule-based bot. Run: python test_free_bot.py"""
from free_bot import FreeBot


def check(question, expected, bot=None):
    reply = (bot or FreeBot()).answer(question)
    assert expected in reply, f"{question!r}: expected {expected!r} in reply:\n{reply}"


check("hi", "Try asking")
check("hey there", "Try asking")
check("List all personas", "5 personas")
check("Tell me about the tech buyers", "### Big-Ticket Tech Buyers")          # 'buyers' must not mean 'buy'
check("Which persona returns the most?", "**Big-Ticket Tech Buyers** has the highest return rate")
check("Which persona uses the most discounts?", "**Deal & Festive Shoppers** has the highest average discount")
check("which persona has the lowest order value", "**Everyday Beauty Shoppers** has the lowest")
check("Compare deal shoppers vs fashion shoppers", "| | Deal & Festive Shoppers | Everyday Fashion Shoppers |")
check("compare fashion", "Which persona should I compare")
check("Which persona should we target for a Diwali campaign?", "start with **Deal & Festive Shoppers**")
check("asdf qwerty", "I'm not sure what you mean")

bot = FreeBot()                                   # follow-up questions remember the persona
check("tell me about beauty shoppers", "### Everyday Beauty Shoppers", bot)
check("where are they?", "**Everyday Beauty Shoppers** by region", bot)    # 'they' must not match 'hey'
check("what do they buy", "by category", bot)
print("All free-bot tests passed")
