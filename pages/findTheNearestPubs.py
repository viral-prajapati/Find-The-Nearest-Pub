import streamlit as st
import pandas as pd
import numpy as np
import folium
from folium import Marker
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static
from app import df

# Load the pub dataset
# pub_data = pd.read_csv('open_pubs.csv', header=None)
# pub_data.columns = ['fsa_id', 'name', 'address', 'postcode', 'easting', 'northing', 'latitude', 'longitude', 'local_authority']

# # Replace \N values with NaN
# pub_data = pub_data.replace('\\N', np.nan)

# # Drop rows with NaN values
# pub_data = pub_data.dropna()

# pub_data['longitude'] = pd.to_numeric(pub_data['longitude'], errors='coerce')
# pub_data['latitude'] = pd.to_numeric(pub_data['latitude'], errors='coerce')

# Set the page layout to centered
st.set_page_config(layout="centered")

# Add some styling to the title and subtitle
st.markdown("<h1 style='text-align: center; color: #fc9003; font-weight: bold;'>Find the Nearest Pub 🍺</h1>", unsafe_allow_html=True)
# st.markdown("<h2 style='text-align: center; color: #5243AA;'></h2>", unsafe_allow_html=True)

# Allow user to enter their latitude and longitude
lat = st.number_input("**Enter latitude:**", value=52.36)
lon = st.number_input("**Enter longitude:**", value=1.16)

# Define a function to calculate the Euclidean distance between two points
def euclidean_distance(lat1, lon1, lat2, lon2):
    return np.sqrt((lat1-lat2)**2 + (lon1-lon2)**2)

# Calculate the distance between the user's location and each pub in the dataset
df['distance'] = df.apply(lambda row: euclidean_distance(row['latitude'], row['longitude'], lat, lon), axis=1)

# Sort the dataset by distance and display the nearest 5 pubs
nearest_pubs = df.sort_values(by='distance').head(5)
st.subheader(f"Top 5 nearest pubs to the given location:")
st.dataframe(nearest_pubs)

# Create a map centered on the user's location
m = folium.Map(location=[lat, lon], zoom_start=13)

# Add a marker for the user's location
folium.Marker(location=[lat, lon], icon=folium.Icon(color='black'), popup='Your Location').add_to(m)

# Add markers for each of the nearest pubs
marker_cluster = MarkerCluster().add_to(m)
for index, row in nearest_pubs.iterrows():
    Marker([row['latitude'], row['longitude']], popup=row['name']).add_to(marker_cluster)

# Display the map
st.subheader("Map of the nearest pubs:")
folium_static(m)

# Add a footer with some information about the app
# st.markdown("<hr>", unsafe_allow_html=True)
# st.write("Data source: https://www.getthedata.com/open-pubs")
# st.sidebar.image('banner_top.png', use_column_width=True)
