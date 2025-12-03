import streamlit as st
import networkx as nx
import folium
from streamlit_folium import folium_static

st.set_page_config(page_title="Province Map", page_icon="🗺️", layout="wide")
st.title("🗺️ Province Cities Graph & Shortest Path")

# --- Sidebar ---
st.sidebar.header("Select Province & Cities")
province = st.sidebar.selectbox("📍 Select Province", ["West Java", "Central Java", "East Java"])
node_color = st.sidebar.color_picker("Node Color", "#FF6347")  # default tomato
edge_color = st.sidebar.color_picker("Edge Color", "#008000")  # default green

# --- Define cities per province ---
province_data = {
    "West Java": {
        "cities": {
            "Jakarta": (-6.2088, 106.8456),
            "Bandung": (-6.9175, 107.6191),
            "Bogor": (-6.5950, 106.8166),
            "Depok": (-6.4025, 106.7944)
        },
        "edges": [
            ("Jakarta", "Bandung", 150),
            ("Jakarta", "Bogor", 60),
            ("Jakarta", "Depok", 40),
            ("Bogor", "Depok", 25),
            ("Bandung", "Depok", 160)
        ]
    },
    "Central Java": {
        "cities": {
            "Semarang": (-6.9667, 110.4167),
            "Solo": (-7.5667, 110.8167),
            "Magelang": (-7.4667, 110.2167),
            "Purwokerto": (-7.4340, 109.2469)
        },
        "edges": [
            ("Semarang", "Solo", 75),
            ("Semarang", "Magelang", 45),
            ("Solo", "Purwokerto", 100),
            ("Magelang", "Purwokerto", 120)
        ]
    },
    "East Java": {
        "cities": {
            "Surabaya": (-7.2575, 112.7521),
            "Malang": (-7.9666, 112.6326),
            "Kediri": (-7.8166, 112.0015),
            "Madiun": (-7.6309, 111.5158)
        },
        "edges": [
            ("Surabaya", "Malang", 90),
            ("Surabaya", "Kediri", 130),
            ("Malang", "Madiun", 120),
            ("Kediri", "Madiun", 80)
        ]
    }
}

# --- Select Cities ---
cities = province_data[province]["cities"]
edges = province_data[province]["edges"]

start_city = st.sidebar.selectbox("🎯 Start City", list(cities.keys()))
end_city = st.sidebar.selectbox("🏁 End City", list(cities.keys()))

# --- Create Graph ---
G = nx.Graph()
for city, coord in cities.items():
    G.add_node(city, pos=coord)
for u, v, w in edges:
    G.add_edge(u, v, weight=w)

# --- Shortest Path ---
if start_city != end_city:
    path = nx.shortest_path(G, source=start_city, target=end_city, weight='weight')
    distance = nx.shortest_path_length(G, source=start_city, target=end_city, weight='weight')

    st.subheader(f"🎯 Shortest Path from {start_city} to {end_city}")
    st.write(f"Path: {' -> '.join(path)}")
    st.write(f"Distance: {distance} km")

    # --- Map Visualization ---
    m = folium.Map(location=cities[start_city], zoom_start=8)

    # Add cities
    for city, coord in cities.items():
        folium.CircleMarker(
            location=coord,
            radius=8,
            popup=city,
            color=node_color,
            fill=True,
            fill_color=node_color
        ).add_to(m)

    # Add shortest path
    path_coords = [cities[city] for city in path]
    folium.PolyLine(
        path_coords,
        color=edge_color,
        weight=5,
        opacity=0.7
    ).add_to(m)

    folium_static(m)

else:
    st.warning("⚠️ Please select different start and end cities")
