import streamlit as st
import pandas as pd
import json
import os

# Set page config as the first command
st.set_page_config(page_title="Fantasy Champions Sportsbook", layout="wide")

# Define JSON file path
json_file_path = "/mnt/data/fantasy_matchup_upload.json"

# Define logo file path
logo_file_path = "/mnt/data/IMG_9766-remove-background.com.png"

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
        background-image: url('/mnt/data/A_sleek,_modern_sportsbook_background_for_Fantasy_.png');
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

# Display Logo (Use fallback if missing)
if os.path.exists(logo_file_path):
    st.image(logo_file_path, width=300)
else:
    st.warning("Logo file missing! Please upload the logo using the uploader below.")
    logo_upload = st.file_uploader("Upload Fantasy Champions Logo", type=["png", "jpg", "jpeg"])
    if logo_upload is not None:
        logo_temp_path = f"/mnt/data/{logo_upload.name}"
        with open(logo_temp_path, "wb") as f:
            f.write(logo_upload.getbuffer())
        st.image(logo_temp_path, width=300)

# Title
st.title("Fantasy Champions Sportsbook")

# Betting Table
st.header("🎯 Fantasy Matchups and Betting Odds")

df = pd.DataFrame(matchup_data)

def get_player_image(player_name):
    image_mapping = {
        "Josh Allen": "/mnt/data/4329ABF7-94BF-4073-8CA8-7ED37302BD69.png",
        "Patrick Mahomes": "/mnt/data/CF878958-A74B-4CCE-881B-6F66B4005940.webp",
        "Saquon Barkley": "/mnt/data/2465146E-65F0-4DFF-8AA4-A812265DFF00.png",
        "Aaron Jones": "/mnt/data/245E185B-E451-4E41-A7B7-E7DB9FBEED2B.png",
        "Nick Chubb": "/mnt/data/356F269A-40E4-4682-96EE-3B3B7A43537A.png",
        "Alvin Kamara": "/mnt/data/7EF876C7-23ED-4749-B846-0F07C60FE08B.png",
        "J'Marr Chase": "/mnt/data/9AB38F34-A00D-4D7F-AF87-DCF8E73C42DB.png",
        "Justin Jefferson": "/mnt/data/6D30D233-E092-4D2C-B1BC-D4226E42029E.png",
        "Courtland Sutton": "/mnt/data/71A3B6FE-ED3D-43EF-8A56-7EB930E120D1.png",
        "Cooper Kupp": "/mnt/data/413956D9-F738-429D-9A0E-B4BBD45F3E8F.png",
        "Travis Kelce": "/mnt/data/2FB9507C-3814-41A7-AF79-B2709C0CBD56.png",
        "Mark Andrews": "/mnt/data/8A064CE0-5AF2-43E1-8D12-BEAF5E969643.png",
        "James Cook": "/mnt/data/E0B44A57-C323-4CD7-AB27-776EF59C780A.png",
        "Brian Thomas": "/mnt/data/7D04C2C5-3FD6-43FC-BF61-143F30F9F811.webp"
    }
    return image_mapping.get(player_name, None)

for index, row in df.iterrows():
    col1, col2, col3, col4 = st.columns([2, 2, 1, 1])
    with col1:
        st.image(get_player_image(row["Team 1 Player"]), width=100)
        st.write(f"**{row['Team 1 Player']}**")
    with col2:
        st.image(get_player_image(row["Team 2 Player"]), width=100)
        st.write(f"**{row['Team 2 Player']}**")
    with col3:
        st.write(f"**Odds:** {row['Team 1 Points']}")
    with col4:
        st.write(f"**Odds:** {row['Team 2 Points']}")
    st.markdown("---")
