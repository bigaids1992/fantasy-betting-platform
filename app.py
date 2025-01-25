import streamlit as st
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

# Sidebar Navigation with Logo and Mock Balance
st.sidebar.image("https://i.imgur.com/STUXtV3.png", width=200)
st.sidebar.title("📌 Navigation")
st.sidebar.write("💰 **Balance: $1,000.00**")
page = st.sidebar.radio("Go to", ["Home", "Fantasy League", "My Bets", "Bet Slip", "Live Tracker"])

# Initialize session state variables
if "bet_slip" not in st.session_state:
    st.session_state.bet_slip = []
if "live_updates" not in st.session_state:
    st.session_state.live_updates = []
if "fantasy_scores" not in st.session_state:
    st.session_state.fantasy_scores = {
        "Josh Allen": 30.5, "Patrick Mahomes": 32.5, "Saquon Barkley": 22.3, "Nick Chubb": 21.4,
        "Aaron Jones": 19.8, "Alvin Kamara": 20.1, "Cooper Kupp": 24.2, "Ja'Marr Chase": 22.7,
        "Courtland Sutton": 17.5, "Justin Jefferson": 26.8, "Travis Kelce": 25.6, "Mark Andrews": 18.9
    }
if "bet_odds" not in st.session_state:
    st.session_state.bet_odds = {"Josh Allen": 150, "Patrick Mahomes": 140, "Saquon Barkley": -110, "Nick Chubb": -120}
if "live_bets" not in st.session_state:
    st.session_state.live_bets = []

# Function to get player images
def get_player_image(player_name):
    image_urls = {
        "Josh Allen": "https://i.imgur.com/Qwe9GQL.png",
        "Patrick Mahomes": "https://i.imgur.com/D2mfI4c.png",
        "Saquon Barkley": "https://i.imgur.com/DEtck1l.png",
        "Nick Chubb": "https://i.imgur.com/9r5Jy24.png",
        "Aaron Jones": "https://i.imgur.com/Z0aXH78.png",
        "Alvin Kamara": "https://i.imgur.com/FJwXv23.png",
        "Cooper Kupp": "https://i.imgur.com/ks8R1Pq.png",
        "Ja'Marr Chase": "https://i.imgur.com/BG7Fy5T.png",
        "Courtland Sutton": "https://i.imgur.com/LpHgD5U.png",
        "Justin Jefferson": "https://i.imgur.com/MqNsEVh.png",
        "Travis Kelce": "https://i.imgur.com/QYHkLZ9.png",
        "Mark Andrews": "https://i.imgur.com/TpMtxRd.png"
    }
    return image_urls.get(player_name, "https://via.placeholder.com/100?text=?")

# Home Page - Predetermined Bets
if page == "Home":
    st.title("Fantasy Champions Sportsbook")
    st.video("https://www.youtube.com/watch?v=3qieRrwAT2c")
    st.button("Sync League")  # Placeholder
    
    st.header("🎯 Predetermined Betting Options")
    for player, odds in st.session_state.bet_odds.items():
        col1, col2, col3 = st.columns([2, 2, 1])
        with col1:
            st.image(get_player_image(player), width=75)
        with col2:
            st.write(f"**{player}** - Odds: {odds}")
        with col3:
            if st.button(f"Bet on {player}", key=f"bet_{player}"):
                st.session_state.bet_slip.append(f"{player} ({odds})")
                st.rerun()

# My Bets Page - Active Bets with Stake, Payout & Cashout
if page == "My Bets":
    st.title("📌 My Active Bets")
    if not st.session_state.live_bets:
        st.write("No active bets at the moment.")
    else:
        for bet in st.session_state.live_bets:
            col1, col2, col3, col4 = st.columns([3, 2, 2, 1])
            with col1:
                st.write(f"✅ {bet}")
            with col2:
                stake = 10  # Mock stake amount
                st.write(f"💸 Stake: ${stake}")
            with col3:
                payout = stake * 2  # Mock payout calculation
                st.write(f"💰 Potential Payout: ${payout}")
            with col4:
                if st.button("Cash Out", key=f"cashout_{bet}"):
                    st.session_state.live_bets.remove(bet)
                    st.success(f"Cashed out: {bet}")
                    st.rerun()

# Bet Slip Page - Display Bets from Home Page with Transfer to My Bets
if page == "Bet Slip":
    st.title("📌 Your Bet Slip")
    if not st.session_state.bet_slip:
        st.write("No bets added yet. Go to the **Home** page to add bets.")
    else:
        for bet in st.session_state.bet_slip:
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write(f"✅ {bet}")
            with col2:
                if st.button("Move to My Bets", key=f"move_{bet}"):
                    st.session_state.live_bets.append(bet)
                    st.session_state.bet_slip.remove(bet)
                    st.rerun()

# Live Tracker Page - Updates Automatically
if page == "Live Tracker":
    st.title("📡 Live Fantasy Tracker")
    players = list(st.session_state.fantasy_scores.keys())
    events = ["scores a touchdown!", "rushes for 10 yards!", "throws a deep pass!", "makes a spectacular catch!", "breaks a tackle for a huge gain!"]
    
    if st.button("Generate Live Update"):
        update = f"{random.choice(players)} {random.choice(events)}"
        st.session_state.live_updates.insert(0, update)
    
    st.write("### Latest Updates:")
    for update in st.session_state.live_updates[:10]:
        st.write(f"- {update}")
