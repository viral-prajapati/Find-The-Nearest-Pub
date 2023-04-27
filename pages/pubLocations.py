import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import folium_static
from app import df

st.markdown("<h1 style='text-align: center; color: #fc9003; font-weight: bold;'>Pub Locations 🍺</h1>", unsafe_allow_html=True)

type = st.radio("**:green[How do you want to search Pub Locations:]**", ('Postal Code', 'Local Authority'))

if type == 'Postal Code':
    list_of = sorted(df['postcode'].unique())
else:
    list_of = sorted(df['local_authority'].unique())

search_val = st.selectbox(f"**:green[Select a {type}:]**", list_of)

if type == 'Postal Code':
    new_data = df[df['postcode'] == search_val]
else:
    new_data = df[df['local_authority'] == search_val]

st.write("**:blue[List of Pubs:]**")
st.dataframe(new_data)

st.write("**:blue[MAP:]**")
map = folium.Map(location=[new_data['latitude'].mean(), new_data['longitude'].mean()], zoom_start=13)

for index, row in new_data.iterrows():
    folium.Marker(location=[row['latitude'], row['longitude']], popup=row['name'],icon=folium.Icon(icon='beer', prefix='fa', color='orange')).add_to(map)

folium_static(map)
