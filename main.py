import streamlit as st
from PIL import Image

col1, col2 = st.columns(2)

with col1:
    image = Image.open('photo.png')
    st.image(image)

with col2:
    st.write("About me")

st.write("These are the collection of apps I have built with Python.")

col3, empty_col, col4 = st.columns([2,1,2])

with col3:
    st.write("Test")

with col4:
    st.write("Test")