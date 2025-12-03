import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import string
import random

st.set_page_config(page_title="Graph Analysis", page_icon="📈", layout="wide")
st.title("📊 Interactive Graph Visualization & Analysis")

# --- Sidebar Input ---
st.sidebar.header("Graph Settings")
num_nodes = st.sidebar.number_input(
    "Enter number of nodes (max 26)", min_value=2, max_value=26, value=5, step=1
)
num_edges = st.sidebar.number_input(
    "Enter number of edges", min_value=1, value=5, step=1
)
node_color = st.sidebar.color_picker("Node Color", "#87CEEB")
edge_color = st.sidebar.color_picker("Edge Color", "#000000")

# --- Generate Nodes ---
nodes = list(string.ascii_uppercase[:num_nodes])

# --- Generate Edges Randomly ---
possible_edges = [
    (u, v) for i, u in enumerate(nodes) for v in nodes[i + 1 :]
]  # all unique combinations

if num_edges > len(possible_edges):
    num_edges = len(possible_edges)

edges = random.sample(possible_edges, num_edges)

# --- Create Graph ---
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# --- Graph Visualization (Compact) ---
st.subheader("📍 Graph Visualization")
pos = nx.spring_layout(G, seed=42)

plt.figure(figsize=(4, 3))
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color=node_color,
    edge_color=edge_color,
    node_size=500,
    font_size=9,
    font_weight="bold",
)
st.pyplot(plt)

# --- Degree of each node ---
st.subheader("🎯 Degree of Each Node")
degrees = dict(G.degree())
st.table(pd.DataFrame(list(degrees.items()), columns=["Node", "Degree"]))

# --- Adjacency Matrix ---
st.subheader("🗂️ Adjacency Matrix")
df_adj = pd.DataFrame(0, index=nodes, columns=nodes)

for u, v in edges:
    df_adj.loc[u, v] = 1
    df_adj.loc[v, u] = 1  # undirected graph

st.dataframe(df_adj)
