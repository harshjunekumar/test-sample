"""Web chat page for the free persona bot.

Run locally:  streamlit run app.py
Host it free: Streamlit Community Cloud (see README).
"""
import streamlit as st

from free_bot import FreeBot
from persona_tools import list_personas

st.set_page_config(page_title="Persona Insights Bot", page_icon="🛒")

EXAMPLES = [
    "List all personas",
    "Tell me about the tech buyers",
    "Which persona returns the most?",
    "Which persona is most at risk of churning?",
    "Compare deal shoppers vs fashion shoppers",
    "Which persona should we target for a Diwali campaign?",
]



def show(text: str) -> None:
    # Escape "$" so Streamlit doesn't treat "$384 ... $883" as a maths formula
    st.markdown(text.replace("$", "\\$"))


if "bot" not in st.session_state:
    st.session_state.bot = FreeBot()
    st.session_state.messages = [{"role": "assistant", "content": st.session_state.bot.help_text()}]

with st.sidebar:
    st.header("👥 Personas")
    for p in list_personas()["personas"]:
        st.markdown(f"**{p['name']}**  \n{p['customers']:,} customers · {p['revenue_share_pct']}% of revenue")
    st.divider()
    st.subheader("Try a question")
    clicked = next((q for q in EXAMPLES if st.button(q, use_container_width=True)), None)
    st.divider()
    st.caption("Free rule-based bot: answers come straight from the customer data. "
               "The data is synthetic, built for a portfolio project.")

st.title("🛒 Persona Insights Bot")
st.caption("Ask about the customer personas of an e-commerce store.")

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        show(m["content"])

question = st.chat_input("Ask about a persona, e.g. 'Which persona uses the most discounts?'") or clicked
if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        show(question)
    reply = st.session_state.bot.answer(question)
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        show(reply)
