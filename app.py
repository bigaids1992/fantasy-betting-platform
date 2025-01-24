import streamlit as st
import pandas as pd
import json

# Configure the app with branding
st.set_page_config(page_title="Fantasy Sportsbook", layout="wide")

# Custom styling for sportsbook look
st.markdown(
    """
    <style>
    body {
        background-color: #0b1a33;
        color: #ffffff;
        font-family: Arial, sans-serif;
    }
    .sidebar .sidebar-content {
        background-color: #1b2a49;
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

# Sidebar Navigation
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/1/12/Fantasy_Football_Logo.png", use_column_width=True)
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Fantasy League", "Bet Slip", "H2H Matchup"])

# Initialize session state for bet slip and fantasy matchup
if "bet_slip" not in st.session_state:
    st.session_state.bet_slip = []
if "fantasy_matchup" not in st.session_state:
    st.session_state.fantasy_matchup = None

# Home Page
if page == "Home":
    st.image("https://upload.wikimedia.org/wikipedia/commons/5/5b/Sports_Betting_Image.jpg", use_column_width=True)
    st.title("🚀 Fantasy-Integrated Sports Betting Platform")
    st.write("Welcome to the next-generation sportsbook where you can bet based on your fantasy league performances!")

    # Betting Options Section
    st.header("🎯 Personalized Betting Odds Based on Your Fantasy Team")
    st.write("Select a bet to add it to your bet slip.")

    # Sample Betting Data with More Props
    betting_data = pd.DataFrame({
        "Player": [
            "Patrick Mahomes", "Patrick Mahomes", "Patrick Mahomes",
            "Saquon Barkley", "Saquon Barkley", "Saquon Barkley",
            "Justin Jefferson", "Justin Jefferson", "Justin Jefferson"
        ],
        "Prop Bet": [
            "Over 300 Passing Yards", "Over 2.5 Passing TDs", "Throw an Interception",
            "Over 1.5 Rushing TDs", "Over 100 Rushing Yards", "Fumble Lost",
            "Over 80 Receiving Yards", "Over 7.5 Receptions", "Score a TD"
        ],
        "Odds": ["+150", "+200", "-110", "+175", "-120", "+250", "-105", "+125", "-110"]
    })

    for index, row in betting_data.iterrows():
        if st.button(f"Add Bet: {row['Player']} - {row['Prop Bet']} ({row['Odds']})"):
            st.session_state.bet_slip.append(f"{row['Player']} - {row['Prop Bet']} ({row['Odds']})")
            st.success(f"Added {row['Player']} - {row['Prop Bet']} to your bet slip!")

# Fantasy League Import Page
elif page == "Fantasy League":
    st.title("📥 Import Your Fantasy League")
    st.write("Sync your **Sleeper, ESPN, or Yahoo Fantasy** league to generate personalized bets.")

    # Mock Fantasy League Import
    uploaded_file = st.file_uploader("Upload Fantasy Matchup JSON File", type=["json"])
    if uploaded_file is not None:
        data = json.load(uploaded_file)
        st.session_state.fantasy_matchup = data
        st.success("Fantasy Matchup Imported Successfully!")

# H2H Matchup Page
elif page == "H2H Matchup":
    st.title("🏈 Head-to-Head Fantasy Matchup")
    if st.session_state.fantasy_matchup:
        matchup = st.session_state.fantasy_matchup
        st.write(f"**{matchup['team_1']} vs {matchup['team_2']}**")
        st.write(f"Projected Points: **{matchup['team_1_score']}** vs **{matchup['team_2_score']}**")
        
        st.subheader("📊 Player Performance Influence on Bets")
        player_data = pd.DataFrame(matchup['players'])
        st.table(player_data)
    else:
        st.write("No fantasy matchup uploaded yet. Go to 'Fantasy League' and upload a JSON file.")

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

st.sidebar.write("🔹 More features coming soon, including real-time odds and fantasy team syncing!")
