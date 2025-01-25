import streamlit as st
import pandas as pd
import json
import os

# Set page config as the first command
st.set_page_config(page_title="Fantasy Champions Sportsbook", layout="wide")

# Define JSON file path
json_file_path = "/mnt/data/fantasy_matchup_upload.json"

# Check if the JSON file exists, else use default data
if os.path.exists(json_file_path):
    with open(json_file_path, "r") as f:
        matchup_data = json.load(f)
else:
    st.warning("Fantasy matchup file not found. Using default data.")
    matchup_data = [
        {"Team 1 Player": "Josh Allen", "Team 1 Points": 28.4, "Team 2 Player": "Patrick Mahomes", "Team 2 Points": 26.22},
        {"Team 1 Player": "Saquon Barkley", "Team 1 Points": 20.6, "Team 2 Player": "Aaron Jones", "Team 2 Points": 19.02}
    ]

# Custom Styling
st.markdown(
    """
    <style>
    body {
        background-size: cover;
        color: white;
    }
    .stButton>button {
        background-color: #ffcc00;
        color: black;
        font-size: 16px;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px;
    }
    .stTable {
        border: 1px solid #ffffff;
        border-radius: 10px;
        overflow: hidden;
    }
    h1, h2, h3 {
        color: #ffcc00;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Image Upload Section for All Images
st.sidebar.header("Upload Images (Logos, Backgrounds, Players, etc.)")
uploaded_files = st.sidebar.file_uploader("Upload Images (PNG, JPG, JPEG)", accept_multiple_files=True, type=["png", "jpg", "jpeg"])
if uploaded_files:
    for uploaded_file in uploaded_files:
        file_path = f"/mnt/data/{uploaded_file.name}"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.sidebar.success(f"Uploaded {uploaded_file.name}")

# Title
st.title("Fantasy Champions Sportsbook")

# Betting Table
st.header("🎯 Fantasy Matchups and Betting Odds")

df = pd.DataFrame(matchup_data)

for index, row in df.iterrows():
    col1, col2, col3, col4 = st.columns([2, 2, 1, 1])
    with col1:
        st.write(f"**{row['Team 1 Player']}**")
    with col2:
        st.write(f"**{row['Team 2 Player']}**")
    with col3:
        st.write(f"**Odds:** {row['Team 1 Points']}")
    with col4:
        st.write(f"**Odds:** {row['Team 2 Points']}")
    st.markdown("---")
