import streamlit as st
import random

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

# Initialize session state for bet slip
if "bet_slip" not in st.session_state:
    st.session_state.bet_slip = []

# Function to get player images
def get_player_image(player_name):
    image_urls = {
        "Josh Allen": "https://i.imgur.com/rvb81LJ.png",
        "Patrick Mahomes": "https://i.imgur.com/D2mfI4c.png",
        "Saquon Barkley": "https://i.imgur.com/DEtck1l.png",
        "Nick Chubb": "https://i.imgur.com/9r5Jy24.png"
    }
    return image_urls.get(player_name, "https://via.placeholder.com/75?text=?")

# Home Page - Predetermined Bets
if page == "Home":
    col1, col2 = st.columns([3, 2])
    with col1:
        st.image("https://i.imgur.com/STUXtV3.png", width=250)
        st.title("Fantasy Champions Sportsbook")
        
        if st.button("Sync League"):
            pass  # Placeholder for future functionality
        
        st.header("🎯 Predetermined Betting Options")
        bets = [
            {"Player": "Josh Allen", "Prop": "Over 250 Passing Yards", "Odds": "+150"},
            {"Player": "Patrick Mahomes", "Prop": "Over 275 Passing Yards", "Odds": "+140"},
            {"Player": "Saquon Barkley", "Prop": "Over 80 Rushing Yards", "Odds": "-110"},
            {"Player": "Nick Chubb", "Prop": "Over 90 Rushing Yards", "Odds": "-120"}
        ]
        
        for bet in bets:
            col1_inner, col2_inner, col3, col4 = st.columns([1, 2, 2, 1])
            with col1_inner:
                st.image(get_player_image(bet['Player']), width=75)
            with col2_inner:
                st.write(f"**{bet['Player']}**")
            with col3:
                st.write(f"💰 {bet['Odds']}")
            with col4:
                if st.button(f"Bet: {bet['Prop']}", key=f"bet_{bet['Player']}"):
                    st.session_state.bet_slip.append(f"{bet['Player']} - {bet['Prop']} ({bet['Odds']})")
                    st.rerun()
            st.markdown("---")
    with col2:
        st.video("https://www.youtube.com/embed/3qieRrwAT2c", start_time=0)

# Fantasy League Page - Hardcoded Matchup
if page == "Fantasy League":
    st.title("📥 Fantasy League Matchup Details")
    st.button("Sync League")  # Placeholder Button
    
    st.header("🏈 The Gridiron Grandpas vs Graveskowski Marches On")
    st.subheader("Projected Score: 151.26 - 85.46")
    
    st.write("### Head-to-Head Matchup")
    players = [
        ("Josh Allen", "QB", "30.5", "Patrick Mahomes", "QB", "32.5"),
        ("Saquon Barkley", "RB", "22.3", "Nick Chubb", "RB", "21.4"),
    ]
    
    for p1, pos1, pts1, p2, pos2, pts2 in players:
        col1, col2, col3 = st.columns([3, 1, 3])
        with col1:
            st.image(get_player_image(p1), width=100)
            st.write(f"**{p1} ({pos1})** - {pts1} Pts")
        with col2:
            st.write("VS")
        with col3:
            st.image(get_player_image(p2), width=100)
            st.write(f"**{p2} ({pos2})** - {pts2} Pts")

# Bet Slip Page - Display Bets from Home Page
if page == "Bet Slip":
    st.title("📌 Your Bet Slip")
    if len(st.session_state.bet_slip) == 0:
        st.write("No bets added yet. Go to the **Home** page to add bets.")
    else:
        st.write("### Your Selected Bets")
        for bet in st.session_state.bet_slip:
            st.write(f"✅ {bet}")

# Live Tracker Page - Generate Hardcoded Live Events
if page == "Live Tracker":
    st.title("📡 Live Fantasy Tracker")
    st.write("Real-time player updates appear here!")
    
    if "live_updates" not in st.session_state:
        st.session_state.live_updates = []
    
    players = ["Josh Allen", "Patrick Mahomes", "Saquon Barkley", "Nick Chubb"]
    events = [
        "scores a touchdown!",
        "rushes for 10 yards!",
        "throws a deep pass!",
        "makes a spectacular catch!",
        "breaks a tackle for a huge gain!"
    ]
    
    if st.button("Generate Live Update"):
        update = f"{random.choice(players)} {random.choice(events)}"
        st.session_state.live_updates.insert(0, update)
    
    st.write("### Latest Updates:")
    for update in st.session_state.live_updates[:10]:
        st.write(f"- {update}")
