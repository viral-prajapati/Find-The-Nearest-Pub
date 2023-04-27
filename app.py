import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('open_pubs.csv', header=None)
df.columns = ['fsa_id', 'name', 'address', 'postcode', 'easting', 'northing', 'latitude', 'longitude', 'local_authority']
df = df.replace('\\N', np.nan)
df = df.dropna()
df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')
df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')

st.balloons()

# My bio data

st.markdown("<h1 style='color: red'>Hello! I am Viral Prajapati</h1>", unsafe_allow_html=True)
st.markdown('''<h5 style='color: blue'>Hi there! I'm Viral Prajapati. I have completed my bachelor's in Information Technology from Government Engineering College, Gandhinagar with an 8.65 CGPA, affiliated with Gujarat Technological University. I'm very interested in industry 4.0 technologies like AI, Machine Learning, Deep Learning, and Blockchain. In addition to having the highest average GPA in my class, I currently work as a Python developer at Code Space Techlabs and have completed two industrial internships, where I gained part-time corporate experience.</h5>''', unsafe_allow_html=True)

st.write("**My Github page:** [Link](https://github.com/viral-prajapati)")

st.write("**My Linkedin page:** [Link](https://www.linkedin.com/in/iamviralprajapati/)")

st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #fc9003; font-weight: bold;'>Open Pub Application 🍺</h1>", unsafe_allow_html=True)
st.image('images/img.jpg', use_column_width=True)

st.markdown("<h2 style='text-align: center; color: orange;'>(Find Pubs in your nearest location)</h2>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: brown; font-weight:bold'>Data Visualization of Pub Data</h2>", unsafe_allow_html=True)
st.markdown("<style>div.stDataFrame div[data-testid='stHorizontalBlock'] div[data-testid='stDataFrameContainer'] {margin: 0 auto;}</style>", unsafe_allow_html=True)
st.write(df.head())

st.subheader('Basic info of the dataset')
st.write(df.dtypes)

st.subheader("Description of the dataset:")
st.write(df.describe())
