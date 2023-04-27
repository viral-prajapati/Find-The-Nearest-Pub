import streamlit as st
import pandas as pd
import numpy as np
import folium
from folium import Marker
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static
from app import df

st.markdown("<h1 style='text-align: center; color: #fc9003; font-weight: bold;'>Find the Nearest Pub 🍺</h1>", unsafe_allow_html=True)

lat = st.number_input("**Enter latitude:**", value=52.36)
lon = st.number_input("**Enter longitude:**", value=1.16)

st.markdown("<hr>", unsafe_allow_html=True)

def el_distance(lat1, lon1, lat2, lon2):
    return np.sqrt((lat1-lat2)**2 + (lon1-lon2)**2)

df['distance'] = df.apply(lambda row: el_distance(row['latitude'], row['longitude'], lat, lon), axis=1)

near_pub_location = df.sort_values(by='distance').head(5)
st.subheader(f":blue[Top 5 nearest pubs to the given location:]")
st.dataframe(near_pub_location)

st.markdown("<hr>", unsafe_allow_html=True)

map = folium.Map(location=[lat, lon], zoom_start=13)

folium.Marker(location=[lat, lon], icon=folium.Icon(color='black'), popup='Your Location').add_to(map)

marker_cluster = MarkerCluster().add_to(map)
for index, row in near_pub_location.iterrows():
    Marker([row['latitude'], row['longitude']], popup=row['name'], icon=folium.Icon(icon='beer', prefix='fa', color='orange')).add_to(marker_cluster)

st.subheader(":blue[Map of the nearest pubs:]")
folium_static(map)
