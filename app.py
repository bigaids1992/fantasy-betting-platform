import streamlit as st
import pandas as pd
import json
import os

# Set page config as the first command
st.set_page_config(page_title="Fantasy Champions Sportsbook", layout="wide")

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Fantasy League", "Bet Slip", "Upload Images"])

# Image Upload Section for Logos, Backgrounds, and Players
st.sidebar.header("Upload Files")
uploaded_files = st.sidebar.file_uploader("Upload Images (Logos, Backgrounds, Players, etc.)", accept_multiple_files=True, type=["png", "jpg", "jpeg"])
if uploaded_files:
    for uploaded_file in uploaded_files:
        file_path = f"/mnt/data/{uploaded_file.name}"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.sidebar.success(f"Uploaded {uploaded_file.name}")

# Upload Fantasy Matchup File
matchup_file = st.sidebar.file_uploader("Upload Fantasy Matchup JSON File", type=["json"])
if matchup_file is not None:
    matchup_data = json.load(matchup_file)
    st.sidebar.success("Fantasy Matchup File Uploaded Successfully!")
else:
    st.warning("No fantasy matchup file uploaded yet. Using default data.")
    matchup_data = [
        {"Team 1 Player": "Josh Allen", "Team 1 Points": 28.4, "Team 2 Player": "Patrick Mahomes", "Team 2 Points": 26.22},
        {"Team 1 Player": "Saquon Barkley", "Team 1 Points": 20.6, "Team 2 Player": "Aaron Jones", "Team 2 Points": 19.02}
    ]

df = pd.DataFrame(matchup_data)

# Home Page
if page == "Home":
    st.title("Fantasy Champions Sportsbook")
    st.header("🎯 Fantasy Matchups and Betting Odds")
    
    for index, row in df.iterrows():
        col1, col2, col3, col4, col5 = st.columns([2, 2, 1, 1, 1])
        with col1:
            st.write(f"**{row['Team 1 Player']}**")
        with col2:
            st.write(f"**{row['Team 2 Player']}**")
        with col3:
            if st.button(f"Bet {row['Team 1 Player']} ({row['Team 1 Points']})", key=f"bet_{index}_1"):
                st.session_state.bet_slip.append(f"{row['Team 1 Player']} - {row['Team 1 Points']}")
        with col4:
            if st.button(f"Bet {row['Team 2 Player']} ({row['Team 2 Points']})", key=f"bet_{index}_2"):
                st.session_state.bet_slip.append(f"{row['Team 2 Player']} - {row['Team 2 Points']}")
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
    st.title("📥 Import Your Fantasy League")
    st.write("Sync your **Sleeper, ESPN, or Yahoo Fantasy** league to generate personalized bets.")
    if matchup_file is not None:
        st.write("Fantasy matchup uploaded and loaded successfully!")
        st.table(df)
    else:
        st.write("No fantasy matchup uploaded yet. Go to 'Upload Images' and upload a JSON file.")

# Upload Images Page
elif page == "Upload Images":
    st.title("📤 Upload and Manage Images")
    st.write("Use the sidebar to upload images for logos, backgrounds, and players.")
    if uploaded_files:
        st.write("### Uploaded Files")
        for uploaded_file in uploaded_files:
            st.write(f"✅ {uploaded_file.name}")
