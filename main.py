import streamlit as st
import pandas

st.set_page_config(layout="wide")

# Create two columns
col1, col2 = st.columns(2)

# First column with my image
with col1:
    st.image("images/photo.png")

# Second column with my description
with col2:
    st.title("Linet Wangui")
    description = """
    Hi. My name is Linet. I am a programmer trying to everything to figure my
    niche. I love penguins🐧 and pandas🐼. I love cakes🎂 I love watching anime
    and bojack horseman."""
    st.info(description)

content2 = """
Below are some of the Python apps I built. Feel free to contact
me in case of any questions.
"""

st.write(content2)

# Pass a list of the ratio dimensions of the columns
col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

# Read data.csv using pandas
data = pandas.read_csv("data.csv", sep=";")

# Display the apps in two columns
# First column
with col3:
    # Specify the rows
    for index, row in data[:10].iterrows():
        # Access the data using the keys
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source code]({row['url']})")


# Second column
with col4:
    for index, row in data[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source code]({row['url']})")

