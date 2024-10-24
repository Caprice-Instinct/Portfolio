import streamlit as st
import pandas

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

content2 = """
Below are some of the Python apps I built. Feel free to contact
me in case of any questions.
"""

st.write(content2)

col3, col4 = st.columns(2)

# Read data.csv using pandas
data = pandas.read_csv("data.csv", sep=";")

# Display the apps in two colums
# First column
with col3:
    for index, row in data[:10].iterrows():
        st.header(row['title'])

# Second column
with col4:
    for index, row in data[10:].iterrows():
        st.header(row['title'])