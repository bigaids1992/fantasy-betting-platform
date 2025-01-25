import streamlit as st
import pandas as pd
import json
from PIL import Image
import openpyxl

# Load fantasy matchup file
def load_fantasy_matchup():
    file_path = "./mnt/data/fantasy_matchup_upload.xlsx"
    df = pd.read_excel(file_path)
    return df

# Mapping player images
player_images = {
    "Josh Allen": "./mnt/data/4329ABF7-94BF-4073-8CA8-7ED37302BD69.png",
    "Patrick Mahomes": "./mnt/data/CF878958-A74B-4CCE-881B-6F66B4005940.webp",
    "Saquon Barkley": "./mnt/data/2465146E-65F0-4DFF-8AA4-A812265DFF00.png",
    "Aaron Jones": "./mnt/data/245E185B-E451-4E41-A7B7-E7DB9FBEED2B.png",
    "Nick Chubb": "./mnt/data/356F269A-40E4-4682-96EE-3B3B7A43537A.png",
    "Alvin Kamara": "./mnt/data/7EF876C7-23ED-4749-B846-0F07C60FE08B.png",
    "Ja'Marr Chase": "./mnt/data/9AB38F34-A00D-4D7F-AF87-DCF8E73C42DB.png",
    "Justin Jefferson": "./mnt/data/6D30D233-E092-4D2C-B1BC-D4226E42029E.png",
    "Courtland Sutton": "./mnt/data/71A3B6FE-ED3D-43EF-8A56-7EB930E120D1.png",
    "Cooper Kupp": "./mnt/data/413956D9-F738-429D-9A0E-B4BBD45F3E8F.png",
    "Travis Kelce": "./mnt/data/2FB9507C-3814-41A7-AF79-B2709C0CBD56.png",
    "Mark Andrews": "./mnt/data/8A064CE0-5AF2-43E1-8D12-BEAF5E969643.png",
    "James Cook": "./mnt/data/E0B44A57-C323-4CD7-AB27-776EF59C780A.png",
    "Brian Thomas": "./mnt/data/7D04C2C5-3FD6-43FC-BF61-143F30F9F811.webp"
}

# App title and background
st.set_page_config(page_title="Fantasy Champions Sportsbook", layout="wide")
st.image("./mnt/data/IMG_9766-remove-background.com.png", width=300)
st.markdown("""
    <style>
        body {
            background-image: url('./mnt/data/A_sleek,_modern_sportsbook_background_for_Fantasy_.png');
            background-size: cover;
        }
    </style>
    """, unsafe_allow_html=True)

# Load matchup data
df = load_fantasy_matchup()
st.title("Fantasy Champions Sportsbook")

# Display matchups
st.write("### Available Bets")
for index, row in df.iterrows():
    team_1_player, team_1_odds, team_2_player, team_2_odds = row["Team 1 Player"], row["Team 1 Points"], row["Team 2 Player"], row["Team 2 Points"]
    
    col1, col2 = st.columns(2)
    with col1:
        st.image(player_images.get(team_1_player, ""), width=100)
        st.write(f"**{team_1_player}**")
        st.write(f"Odds: {team_1_odds}")
        if st.button(f"Bet on {team_1_player}", key=f"bet_{index}_1"):
            st.session_state.bet_slip.append((team_1_player, team_1_odds))
    
    with col2:
        st.image(player_images.get(team_2_player, ""), width=100)
        st.write(f"**{team_2_player}**")
        st.write(f"Odds: {team_2_odds}")
        if st.button(f"Bet on {team_2_player}", key=f"bet_{index}_2"):
            st.session_state.bet_slip.append((team_2_player, team_2_odds))

# Display bet slip
st.write("### Your Bet Slip")
if "bet_slip" not in st.session_state:
    st.session_state.bet_slip = []

if len(st.session_state.bet_slip) == 0:
    st.write("No bets placed yet.")
else:
    for bet in st.session_state.bet_slip:
        st.write(f"✅ {bet[0]} - Odds: {bet[1]}")

    bet_amount = st.number_input("Enter Bet Amount ($):", min_value=1, value=10)
    potential_payout = bet_amount * sum(float(b[1]) for b in st.session_state.bet_slip)
    st.success(f"Your potential payout: **${potential_payout:.2f}**")

    if st.button("Clear Bet Slip"):
        st.session_state.bet_slip = []
        st.experimental_rerun()
