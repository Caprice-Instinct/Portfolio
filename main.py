import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Linet Wangui")
    content = """
    Hi. My name is Linet. I am a programmer trying to everything to figure my
    niche. I love penguins🐧 and pandas🐼. I love cakes🎂 I love watching anime
    and bojack horseman."""
    st.info(content)