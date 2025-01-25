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
        {"Player": "Josh Allen", "Position": "QB", "Fantasy Points": 30.5, "Projected Prop": "Over 250 Passing Yards", "Odds": "+150"},
        {"Player": "Patrick Mahomes", "Position": "QB", "Fantasy Points": 32.5, "Projected Prop": "Over 275 Passing Yards", "Odds": "+140"},
        {"Player": "Saquon Barkley", "Position": "RB", "Fantasy Points": 22.3, "Projected Prop": "Over 80 Rushing Yards", "Odds": "-110"},
        {"Player": "Nick Chubb", "Position": "RB", "Fantasy Points": 21.4, "Projected Prop": "Over 90 Rushing Yards", "Odds": "-120"}
    ]
}

# Function to get player image from external hosting
def get_player_image(player_name):
    image_urls = {
        "Josh Allen": "https://i.imgur.com/rvb81LJ.png",
        "Patrick Mahomes": "https://i.imgur.com/D2mfI4c.png",
        "Saquon Barkley": "https://i.imgur.com/DEtck1l.png",
        "Nick Chubb": "https://i.imgur.com/9r5Jy24.png"
    }
    return image_urls.get(player_name, "https://via.placeholder.com/75?text=?")

# Home Page - Display Betting Options and Video
if page == "Home":
    col1, col2 = st.columns([3, 1])
    with col1:
        st.image("https://i.imgur.com/STUXtV3.png", width=250)
        st.title("Fantasy Champions Sportsbook")
        
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
                    st.success(f"Added {player['Player']} - {player['Projected Prop']} to Bet Slip!")
            st.markdown("---")
    with col2:
        st.video("https://www.youtube.com/embed/3qieRrwAT2c")

# Live Tracker Page - Generate Live Events
if page == "Live Tracker":
    st.title("📡 Live Fantasy Tracker")
    st.write("Real-time player updates appear here!")
    
    players = [player["Player"] for player in matchup_data["players"]]
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
    
    st.write("### Latest Updates:")
    for update in st.session_state.live_updates[:10]:
        st.write(f"- {update}")
