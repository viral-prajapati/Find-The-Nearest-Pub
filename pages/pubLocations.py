import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import folium_static
from app import df

st.markdown("<h1 style='text-align: center; color: #fc9003; font-weight: bold;'>Pub Locations 🍺</h1>", unsafe_allow_html=True)

search_type = st.radio("**:green[How do you want to search Pub Locations:]**", ('Postal Code', 'Local Authority'))

if search_type == 'Postal Code':
    search_list = sorted(df['postcode'].unique())
else:
    search_list = sorted(df['local_authority'].unique())

search_value = st.selectbox(f"**:green[Select a {search_type}:]**", search_list)

if search_type == 'Postal Code':
    filtered_data = df[df['postcode'] == search_value]
else:
    filtered_data = df[df['local_authority'] == search_value]

st.write("**:blue[List of Pubs:]**")
st.dataframe(filtered_data)

st.write("**:blue[MAP:]**")
map = folium.Map(location=[filtered_data['latitude'].mean(), filtered_data['longitude'].mean()], zoom_start=13)

for index, row in filtered_data.iterrows():
    folium.Marker(location=[row['latitude'], row['longitude']], popup=row['name'],icon=folium.Icon(icon='beer', prefix='fa', color='orange')).add_to(map)

folium_static(map)
