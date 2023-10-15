import streamlit as st
from PIL import Image
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    image = Image.open('images/photo.png')
    st.image(image)

with col2:
    st.write("About me")
    content = """In the Name of Allah, the Most Beneficent, 
    the Most Merciful. All the praises and thanks be to Allah, 
    the Lord of the 'Alamin (mankind, jinns and all that exists). 
    The Most Beneficent, the Most Merciful. The Only Owner (and the 
    Only Ruling Judge) of the Day of Recompense (i.e. the Day of 
    Resurrection). You (Alone) we worship, and You (Alone) we ask 
    for help (for each and everything). Guide us to the Straight 
    Way. The Way of those on whom You have bestowed Your Grace, 
    not (the way) of those who earned Your Anger (such as the 
    Jews), nor of those who went astray (such as the Christians). """
    st.write(content)

st.title("These are the collection of apps I have built with Python.")

col3, empty_col, col4 = st.columns([2,1,2])
data = pd.read_csv('data.csv',sep=';')

with col3:
    for index, row in data[0:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        image = Image.open(f"images/{row['image']}")
        st.image(image)
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in data[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        image = Image.open(f"images/{row['image']}")
        st.image(image)
        st.write(f"[Source Code]({row['url']})")
