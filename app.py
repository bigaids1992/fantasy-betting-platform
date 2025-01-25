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

# Initialize session state for bet slip, matchup data, and live tracker
if "bet_slip" not in st.session_state:
    st.session_state.bet_slip = []
if "matchup_data" not in st.session_state:
    st.session_state.matchup_data = {}
if "live_updates" not in st.session_state:
    st.session_state.live_updates = []
if "matchup_updates" not in st.session_state:
    st.session_state.matchup_updates = []

# Upload Fantasy Matchup File
matchup_file = st.sidebar.file_uploader("Upload Fantasy Matchup JSON File", type=["json"])
if matchup_file is not None:
    try:
        matchup_json = json.load(matchup_file)
        if "team_1" in matchup_json and "players" in matchup_json:
            st.session_state.matchup_data = matchup_json
            st.session_state.live_updates = []  # Reset live updates
            st.session_state.matchup_updates = []  # Reset matchup updates
            st.sidebar.success("Fantasy Matchup File Uploaded Successfully!")
        else:
            st.sidebar.error("Invalid JSON structure. Please upload a valid matchup file.")
    except Exception as e:
        st.sidebar.error(f"Error processing JSON file: {e}")

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
        "James Cook": "https://i.imgur.com/HOtD9bm.png",
        "Patrick Mahomes": "https://i.imgur.com/D2mfI4c.png",
        "Brian Thomas": "https://i.imgur.com/baDCucV.png"
    }
    return image_urls.get(player_name, "https://via.placeholder.com/75?text=?")

# Fantasy League Page - Display Matchup Data Side-by-Side
if page == "Fantasy League":
    st.title("📥 Fantasy League Matchup Details")
    matchup_data = st.session_state.get("matchup_data", {})
    if matchup_data and "players" in matchup_data:
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

# Live Tracker Page - Generate Live Events
if page == "Live Tracker":
    st.title("📡 Live Fantasy Tracker")
    st.write("Real-time player updates appear here!")
    
    players = [player["Player"] for player in st.session_state.get("matchup_data", {}).get("players", [])]
    events = [
        "scores a touchdown!",
        "rushes for 10 yards!",
        "throws a deep pass!",
        "makes a spectacular catch!",
        "breaks a tackle for a huge gain!"
    ]
    
    if st.button("Generate Live Update"):
        if players:
            update = f"{random.choice(players)} {random.choice(events)}"
            st.session_state.live_updates.insert(0, update)
        else:
            update = "Waiting for matchup data..."
            st.session_state.live_updates.insert(0, update)
    
    st.write("### Latest Updates:")
    for update in st.session_state.live_updates[:10]:
        st.write(f"- {update}")

    if st.button("Generate Another Update"):
        if players:
            update = f"{random.choice(players)} {random.choice(events)}"
            st.session_state.live_updates.insert(0, update)
