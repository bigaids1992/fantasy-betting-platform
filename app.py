import streamlit as st
import random

# Set page config
st.set_page_config(page_title="Fantasy Champions Sportsbook", layout="wide")

# Sidebar Navigation
st.sidebar.image("https://i.imgur.com/STUXtV3.png", width=200)
st.sidebar.title("📌 Navigation")
st.sidebar.write("💰 **Balance: $1,000.00**")
page = st.sidebar.radio("Go to", ["Home", "Fantasy League", "My Bets", "Bet Slip", "Live Tracker"])

# Function to get player images
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
    return image_urls.get(player_name, "https://via.placeholder.com/100?text=?")

# Fantasy Scores
fantasy_scores = {
    "Josh Allen": 30.5, "Patrick Mahomes": 32.5, "Saquon Barkley": 22.3, "Nick Chubb": 21.4,
    "Aaron Jones": 19.8, "Alvin Kamara": 20.1, "Cooper Kupp": 24.2, "J Chase": 22.7,
    "Courtland Sutton": 17.5, "Justin Jefferson": 26.8, "Travis Kelce": 25.6, "Mark Andrews": 18.9
}

# Home Page - Predetermined Bets
if page == "Home":
    st.title("Fantasy Champions Sportsbook")
    st.video("https://www.youtube.com/watch?v=3qieRrwAT2c")
    st.button("Sync League")
    
    st.header("🎯 Betting Options")
    bets = [
        ("Josh Allen", "+150"), ("Saquon Barkley", "-110"), ("Nick Chubb", "-120"),
        ("Cooper Kupp", "+125"), ("J Chase", "+135"), ("Travis Kelce", "+175")
    ]
    for player, odds in bets:
        col1, col2, col3 = st.columns([2, 2, 1])
        with col1:
            st.image(get_player_image(player), width=75)
        with col2:
            st.write(f"**{player}** - Odds: {odds}")
        with col3:
            if st.button(f"Bet on {player}", key=f"bet_{player}"):
                st.session_state.bet_slip.append((player, odds))
                st.rerun()

# Fantasy League Page - Hardcoded Matchup
if page == "Fantasy League":
    st.title("📥 Fantasy League Matchup")
    st.button("Sync League")
    
    st.header("🏈 Matchup Lineup")
    matchups = [
        ("Josh Allen", "Patrick Mahomes"), ("Saquon Barkley", "Nick Chubb"), ("Aaron Jones", "Alvin Kamara"),
        ("Cooper Kupp", "J Chase"), ("Courtland Sutton", "Justin Jefferson"), ("Travis Kelce", "Mark Andrews")
    ]
    for player1, player2 in matchups:
        col1, col2, col3 = st.columns([3, 1, 3])
        with col1:
            st.image(get_player_image(player1), width=100)
            st.write(f"**{player1}** - Fantasy Points: {fantasy_scores.get(player1, 'N/A')}")
        with col2:
            st.write("VS")
        with col3:
            st.image(get_player_image(player2), width=100)
            st.write(f"**{player2}** - Fantasy Points: {fantasy_scores.get(player2, 'N/A')}")

# Live Tracker Page
if page == "Live Tracker":
    st.title("📡 Live Fantasy Tracker")
    players = list(fantasy_scores.keys())
    events = ["scores a touchdown!", "rushes for 10 yards!", "throws a deep pass!", "makes a spectacular catch!", "breaks a tackle for a huge gain!"]
    
    if "live_updates" not in st.session_state:
        st.session_state.live_updates = []
    
    if st.button("Generate Live Update"):
        update = f"{random.choice(players)} {random.choice(events)}"
        st.session_state.live_updates.insert(0, update)
    
    st.write("### Latest Updates:")
    for update in st.session_state.live_updates[:10]:
        st.write(f"- {update}")
