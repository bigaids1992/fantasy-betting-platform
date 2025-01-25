import streamlit as st
import pandas as pd
import json

# Set page config as the first command
st.set_page_config(page_title="Fantasy Champions Sportsbook", layout="wide")

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Fantasy League", "Bet Slip"])

# Initialize session state for bet slip
if "bet_slip" not in st.session_state:
    st.session_state.bet_slip = []
if "matchup_data" not in st.session_state:
    st.session_state.matchup_data = {}

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
        "Josh Allen": "https://i.imgur.com/Qwe9GQL.png"
    }
    return image_urls.get(player_name, "https://via.placeholder.com/75?text=?")

# Home Page
if page == "Home":
    st.title("Fantasy Champions Sportsbook")
    matchup_data = st.session_state.get("matchup_data", {})
    if matchup_data:
        st.header(f"🏈 {matchup_data.get('team_1', 'Team 1')} vs {matchup_data.get('team_2', 'Team 2')}")
        st.subheader(f"Projected Score: {matchup_data.get('team_1_score', 0)} - {matchup_data.get('team_2_score', 0)}")
        
        st.header("🎯 Fantasy Player Props & Betting Odds")
        for player in matchup_data.get("players", []):
            col1, col2, col3, col4, col5 = st.columns([1, 2, 2, 1, 1])
            with col1:
                img_url = get_player_image(player['Player'])
                st.image(img_url, width=75)
            with col2:
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

# Bet Slip Page
elif page == "Bet Slip":
    st.title("📌 Your Bet Slip")
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
    matchup_data = st.session_state.get("matchup_data", {})
    if matchup_data:
        st.header(f"🏈 {matchup_data.get('team_1', 'Team 1')} vs {matchup_data.get('team_2', 'Team 2')}")
        st.subheader(f"Projected Score: {matchup_data.get('team_1_score', 0)} - {matchup_data.get('team_2_score', 0)}")
        st.write("### Player Data")
        
        for player in matchup_data.get("players", []):
            col1, col2 = st.columns([1, 4])
            with col1:
                img_url = get_player_image(player['Player'])
                st.image(img_url, width=75)
            with col2:
                st.write(f"**{player['Player']}** - Fantasy Points: {player['Fantasy Points']}, Prop: {player['Projected Prop']}, Odds: {player['Odds']}")
