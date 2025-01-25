import streamlit as st
import pandas as pd
import json
import random
import time

# Set page config with background styling
st.set_page_config(page_title="Fantasy Champions Sportsbook", layout="wide")

# Apply background image styling
page_bg_img = f'''
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("https://i.imgur.com/G0Hb2PZ.png");
    background-size: cover;
    background-position: center;
}}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Sidebar Navigation with Logo
st.sidebar.image("https://i.imgur.com/STUXtV3.png", width=200)
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Fantasy League", "Bet Slip", "Live Tracker"])

# Hardcoded Matchup Data for Demo Purposes
matchup_data = {
    "team_1": "The Gridiron Grandpas",
    "team_2": "Graveskowski Marches On",
    "team_1_score": 151.26,
    "team_2_score": 85.46,
    "players": [
        {"Player": "Josh Allen", "Position": "QB", "Fantasy Points": 30.5},
        {"Player": "Patrick Mahomes", "Position": "QB", "Fantasy Points": 32.5},
        {"Player": "Saquon Barkley", "Position": "RB", "Fantasy Points": 22.3},
        {"Player": "Nick Chubb", "Position": "RB", "Fantasy Points": 21.4},
        {"Player": "Aaron Jones", "Position": "RB", "Fantasy Points": 19.8},
        {"Player": "Alvin Kamara", "Position": "RB", "Fantasy Points": 20.1},
        {"Player": "Cooper Kupp", "Position": "WR", "Fantasy Points": 24.2},
        {"Player": "J Chase", "Position": "WR", "Fantasy Points": 22.7},
        {"Player": "Courtland Sutton", "Position": "WR", "Fantasy Points": 17.5},
        {"Player": "Justin Jefferson", "Position": "WR", "Fantasy Points": 26.8},
        {"Player": "Travis Kelce", "Position": "TE", "Fantasy Points": 25.6},
        {"Player": "Mark Andrews", "Position": "TE", "Fantasy Points": 18.9}
    ]
}

# Function to get player image from external hosting
def get_player_image(player_name):
    image_urls = {
        "Josh Allen": "https://i.imgur.com/rvb81LJ.png",
        "Saquon Barkley": "https://i.imgur.com/DEtck1l.png",
        "Aaron Jones": "https://i.imgur.com/XjPiGiI.png",
        "Nick Chubb": "https://i.imgur.com/9r5Jy24.png",
        "Alvin Kamara": "https://i.imgur.com/wc4NTJa.png",
        "Courtland Sutton": "https://i.imgur.com/vn2hnCM.png",
        "Cooper Kupp": "https://i.imgur.com/jnMoGV3.png",
        "Travis Kelce": "https://i.imgur.com/MwJTFjD.png",
        "Mark Andrews": "https://i.imgur.com/H4iiyPd.png",
        "J Chase": "https://i.imgur.com/lnV5QCp.png",
        "Justin Jefferson": "https://i.imgur.com/ofyGZiM.png",
        "Patrick Mahomes": "https://i.imgur.com/D2mfI4c.png"
    }
    return image_urls.get(player_name, "https://via.placeholder.com/75?text=?")

# Fantasy League Page - Display Hardcoded Matchup Data
if page == "Fantasy League":
    st.title("📥 Fantasy League Matchup Details")
    st.button("Sync League")  # Placeholder Button
    
    st.header(f"🏈 {matchup_data['team_1']} vs {matchup_data['team_2']}")
    st.subheader(f"Projected Score: {matchup_data['team_1_score']} - {matchup_data['team_2_score']}")
    
    st.write("### Head-to-Head Matchup")
    for i in range(0, len(matchup_data["players"]), 2):
        col1, col2, col3 = st.columns([3, 1, 3])
        with col1:
            player1 = matchup_data["players"][i]
            st.image(get_player_image(player1['Player']), width=100)
            st.write(f"**{player1['Player']} ({player1['Position']})**")
            st.write(f"Fantasy Points: {player1['Fantasy Points']}")
        with col2:
            st.write("VS")
        with col3:
            if i+1 < len(matchup_data["players"]):
                player2 = matchup_data["players"][i+1]
                st.image(get_player_image(player2['Player']), width=100)
                st.write(f"**{player2['Player']} ({player2['Position']})**")
                st.write(f"Fantasy Points: {player2['Fantasy Points']}")

    st.write("---")
    st.write("✅ Matchup Data is now **always available**, no upload required!")
