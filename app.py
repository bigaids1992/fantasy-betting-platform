import streamlit as st
import pandas as pd
import json
import os

# Set page config as the first command
st.set_page_config(page_title="Fantasy Champions Sportsbook", layout="wide")

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Fantasy League", "Bet Slip", "Upload Images"])

# Upload Fantasy Matchup File
matchup_file = st.sidebar.file_uploader("Upload Fantasy Matchup JSON File", type=["json"])
if matchup_file is not None:
    matchup_data = json.load(matchup_file)
    st.sidebar.success("Fantasy Matchup File Uploaded Successfully!")
else:
    st.warning("No fantasy matchup file uploaded yet. Using default data.")
    matchup_data = {
        "team_1": "Warriors",
        "team_2": "Titans",
        "team_1_score": 125.7,
        "team_2_score": 118.3,
        "players": [
            {"Player": "Josh Allen", "Fantasy Points": 26.4, "Projected Prop": "Over 275 Passing Yards", "Odds": "+150"},
            {"Player": "Derrick Henry", "Fantasy Points": 21.1, "Projected Prop": "Over 100 Rushing Yards", "Odds": "+175"},
            {"Player": "Davante Adams", "Fantasy Points": 19.8, "Projected Prop": "Over 85 Receiving Yards", "Odds": "+120"},
            {"Player": "Travis Kelce", "Fantasy Points": 17.5, "Projected Prop": "Over 6.5 Receptions", "Odds": "-110"},
            {"Player": "Justin Jefferson", "Fantasy Points": 22.9, "Projected Prop": "Over 90 Receiving Yards", "Odds": "+140"},
            {"Player": "Patrick Mahomes", "Fantasy Points": 24.1, "Projected Prop": "Over 2.5 Passing TDs", "Odds": "+130"}
        ]
    }

# Image Upload Section
st.sidebar.header("Upload Player Images")
image_files = st.sidebar.file_uploader("Upload Player Images (PNG, JPG, JPEG)", accept_multiple_files=True, type=["png", "jpg", "jpeg"])
if image_files:
    for image in image_files:
        file_path = f"/mnt/data/{image.name}"
        with open(file_path, "wb") as f:
            f.write(image.getbuffer())
    st.sidebar.success("Images Uploaded Successfully!")

# Function to find the player's image file
def get_player_image(player_name):
    formatted_name = player_name.replace(" ", "_")
    for ext in ["png", "jpg", "jpeg"]:
        file_path = f"/mnt/data/{formatted_name}.{ext}"
        if os.path.exists(file_path):
            return file_path
    return None  # No image found

# Home Page
if page == "Home":
    st.title("Fantasy Champions Sportsbook")
    st.header(f"🏈 {matchup_data['team_1']} vs {matchup_data['team_2']}")
    st.subheader(f"Projected Score: {matchup_data['team_1_score']} - {matchup_data['team_2_score']}")
    
    st.header("🎯 Fantasy Player Props & Betting Odds")
    
    for player in matchup_data["players"]:
        col1, col2, col3, col4, col5 = st.columns([1, 2, 2, 1, 1])
        with col1:
            img_path = get_player_image(player['Player'])
            if img_path:
                st.image(img_path, width=75)
        with col2:
            st.write(f"**{player['Player']}**")
        with col3:
            st.write(f"📊 Fantasy Points: {player['Fantasy Points']}")
        with col4:
            st.write(f"💰 Odds: {player['Odds']}")
        with col5:
            if st.button(f"Bet: {player['Projected Prop']}", key=f"bet_{player['Player']}"):
                if "bet_slip" not in st.session_state:
                    st.session_state.bet_slip = []
                st.session_state.bet_slip.append(f"{player['Player']} - {player['Projected Prop']} ({player['Odds']})")
                st.success(f"Added {player['Player']} - {player['Projected Prop']} to Bet Slip!")
        st.markdown("---")

# Bet Slip Page
elif page == "Bet Slip":
    st.title("📌 Your Bet Slip")
    if "bet_slip" not in st.session_state:
        st.session_state.bet_slip = []
    
    if len(st.session_state.bet_slip) == 0:
        st.write("No bets added yet. Go to the **Home** page to add bets.")
    else:
        st.write("### Your Selected Bets")
        for bet in st.session_state.bet_slip:
            st.write(f"✅ {bet}")
        st.write("---")
        bet_amount = st.number_input("Enter Bet Amount ($):", min_value=1, value=10)
        if st.button("Calculate Potential Payout"):
            st.success(f"Your potential payout: **${bet_amount * 2}** (Mock Calculation)")
        if st.button("Clear Bet Slip"):
            st.session_state.bet_slip = []
            st.success("Bet slip cleared!")

# Fantasy League Page
elif page == "Fantasy League":
    st.title("📥 Fantasy League Matchup Details")
    st.header(f"🏈 {matchup_data['team_1']} vs {matchup_data['team_2']}")
    st.subheader(f"Projected Score: {matchup_data['team_1_score']} - {matchup_data['team_2_score']}")
    st.write("### Player Data")
    st.table(pd.DataFrame(matchup_data["players"]))

# Upload Images Page
elif page == "Upload Images":
    st.title("📤 Upload and Manage Images")
    st.write("Use the sidebar to upload images for logos, backgrounds, and players.")
