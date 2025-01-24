import streamlit as st
import pandas as pd

# Configure the app
st.set_page_config(page_title="Fantasy Sportsbook", layout="wide")

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Fantasy League", "Bet Slip"])

# Initialize session state for bet slip
if "bet_slip" not in st.session_state:
    st.session_state.bet_slip = []

# Home Page
if page == "Home":
    st.title("🚀 Fantasy-Integrated Sports Betting Platform")
    st.write("Welcome to the next-generation sportsbook where you can bet based on your fantasy league performances!")

    # Betting Options Section
    st.header("🎯 Personalized Betting Odds Based on Your Fantasy Team")
    st.write("Select a bet to add it to your bet slip.")

    # Sample Betting Data
    betting_data = pd.DataFrame({
        "Player": ["Patrick Mahomes", "Saquon Barkley", "Justin Jefferson"],
        "Prop Bet": ["Over 300 Passing Yards", "Over 1.5 Rushing TDs", "Over 80 Receiving Yards"],
        "Odds": ["+150", "+200", "-110"]
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
    fantasy_league = st.text_input("Enter your Fantasy League ID (Mock for now):")
    if st.button("Import League"):
        st.success(f"Fantasy League {fantasy_league} imported successfully! (Feature will be dynamic in Phase 2)")

# Bet Slip Page
elif page == "Bet Slip":
    st.title("📌 Your Bet Slip")
    if len(st.session_state.bet_slip) == 0:
        st.write("No bets added yet. Go to the **Home** page to add bets.")
    else:
        for bet in st.session_state.bet_slip:
            st.write(f"✅ {bet}")
        if st.button("Clear Bet Slip"):
            st.session_state.bet_slip = []
            st.success("Bet slip cleared!")

st.sidebar.write("🔹 More features coming soon, including real-time odds and fantasy team syncing!")

