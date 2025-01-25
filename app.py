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
        st.session_state.matchup_data = json.load(matchup_file)
        st.sidebar.success("Fantasy Matchup File Uploaded Successfully!")
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

# Home Page - Display Bets from Matchup Data
if page == "Home":
    col1, col2 = st.columns([3, 1])
    with col1:
        st.image("https://i.imgur.com/STUXtV3.png", width=250)  # Display logo prominently
        st.title("Fantasy Champions Sportsbook")
        matchup_data = st.session_state.get("matchup_data", {})
        if matchup_data and "players" in matchup_data:
            st.header(f"🏈 {matchup_data['team_1']} vs {matchup_data['team_2']}")
            st.subheader(f"Projected Score: {matchup_data['team_1_score']} - {matchup_data['team_2_score']}")
            
            st.header("🎯 Fantasy Player Props & Betting Odds")
            for player in matchup_data["players"]:
                col1_inner, col2_inner, col3, col4, col5 = st.columns([1, 2, 2, 1, 1])
                with col1_inner:
                    img_url = get_player_image(player['Player'])
                    st.image(img_url, width=75)
                with col2_inner:
                    st.write(f"**{player['Player']}**")
                with col3:
                    st.write(f"📊 Fantasy Points: {player['Fantasy Points']}")
                with col4:
                    st.write(f"💰 Odds: {player['Odds']}")
                with col5:
                    if st.button(f"Bet: {player['Projected Prop']}", key=f"bet_{player['Player']}"):
                        st.session_state.bet_slip.append(f"{player['Player']} - {player['Projected Prop']} ({player['Odds']})")
                        st.sidebar.success(f"Added {player['Player']} - {player['Projected Prop']} to Bet Slip!")
                st.markdown("---")
    with col2:
        st.video("https://www.youtube.com/embed/kYhSZTAWvcg")  # Updated YouTube video URL
