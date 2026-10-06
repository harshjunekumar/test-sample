""""Just for you": a free fashion styling chatbot (Streamlit web app).

Run locally:  streamlit run app.py
"""
import streamlit as st

from stylist import Stylist

st.set_page_config(page_title="Just for you | Personal Stylist", page_icon="👗", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Poppins:wght@300;500&display=swap');
.jfy-logo {text-align:center; margin: -1rem 0 0.5rem;}
.jfy-logo .script {font-family:'Great Vibes', cursive; font-size:3.6rem; line-height:1.1;
                   background:linear-gradient(90deg,#B23A6F,#D9822B); -webkit-background-clip:text;
                   background-clip:text; color:transparent;}
.jfy-logo .tag {font-family:'Poppins', sans-serif; font-weight:300; letter-spacing:0.35em;
                font-size:0.75rem; color:#8A6F7A; text-transform:uppercase;}
.stChatMessage h4 {font-size:1.05rem; padding:0.6rem 0 0.2rem;}
[data-testid="stHeaderActionElements"] {display:none;}
.swatches {display:flex; gap:14px; flex-wrap:wrap; margin:4px 0 10px;}
.swatch {text-align:center; font-size:0.75rem; color:#666; width:72px;}
.swatch span {display:block; width:44px; height:44px; border-radius:50%; margin:0 auto 4px;
              border:1px solid rgba(0,0,0,0.12);}
</style>
<div class="jfy-logo">
  <div class="script">Just for you</div>
  <div class="tag">✦ your personal stylist ✦</div>
</div>
""", unsafe_allow_html=True)

if "stylist" not in st.session_state:
    st.session_state.stylist = Stylist()
    st.session_state.messages = [{"role": "assistant", **st.session_state.stylist.greeting()}]


def send(text: str) -> None:
    st.session_state.messages.append({"role": "user", "text": text})
    st.session_state.messages.append({"role": "assistant", **st.session_state.stylist.reply(text)})


def show_palette(palette) -> None:
    chips = "".join(f'<div class="swatch"><span style="background:{hex_}"></span>{name}</div>'
                    for name, hex_ in palette)
    st.markdown(f'<div class="swatches">{chips}</div>', unsafe_allow_html=True)


for m in st.session_state.messages:
    with st.chat_message(m["role"], avatar="👗" if m["role"] == "assistant" else None):
        if m.get("palette"):          # show the colour swatches right under the palette section
            before, after = m["text"].split("#### 💡", 1)
            st.markdown(before)
            show_palette(m["palette"])
            st.markdown("#### 💡" + after)
        else:
            st.markdown(m["text"])

# Quick-reply buttons for the current question
options = st.session_state.stylist.options()
for row in range(0, len(options), 3):     # rows of 3, so the order stays right on phones too
    cols = st.columns(3)
    for col, option in zip(cols, options[row:row + 3]):
        if col.button(option, key=f"opt-{len(st.session_state.messages)}-{option}", use_container_width=True):
            send(option)
            st.rerun()

typed = st.chat_input("Type your answer, e.g. 'female, 28' or 'show me pastels'")
if typed:
    send(typed)
    st.rerun()

st.caption("Recommendations are style ideas, not ads. 'Shop on Google' opens live Google Shopping results. "
           "Trends researched from fashion sites on Google, October 2026.")
