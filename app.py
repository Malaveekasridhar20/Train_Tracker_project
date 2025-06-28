import streamlit as st
import pandas as pd
from googletrans import Translator
import telegram
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID, PUSHBULLET_API_KEY
from pushbullet_alert import send_pushbullet_alert
import os
from urllib.parse import quote

# ✅ IRCTC booking link helper
def show_alternative_link(from_station, to_station, date_str):
    """
    Show IRCTC link to book alternate trains.
    Example: from_station = 'TPJ', to_station = 'MS', date_str = '27-06-2025'
    """
    url = f"https://www.irctc.co.in/nget/train-search?from={quote(from_station)}&to={quote(to_station)}&journeyDate={quote(date_str)}"
    st.warning("🚨 Your train is delayed. Book an alternative train below:")
    st.markdown(f"[🔁 Book Alternate Train]({url})", unsafe_allow_html=True)

# ✅ Set Streamlit page config
st.set_page_config(page_title="🚆 Train Tracker + Alerts", layout="centered")

# Translator setup
translator = Translator()

# ✅ Ensure data folder exists
os.makedirs("data", exist_ok=True)

# Load CSV
@st.cache_data
def load_data():
    df = pd.read_csv("data/train_status_data.csv")
    df['train_no'] = df['train_no'].astype(str)
    return df

df = load_data()

# 🚆 UI
st.title("🚆 Train Status Tracker")
st.markdown("Check live train status and send alerts in your language.\nIncludes link for 🍽️ food preference form.")

# Language selection
lang_name_to_code = {
    "English": "en",
    "Tamil - தமிழ்": "ta",
    "Hindi - हिन्दी": "hi",
    "Telugu - తెలుగు": "te",
    "Kannada - ಕನ್ನಡ": "kn",
    "Marathi - मराठी": "mr",
    "Bengali - বাংলা": "bn"
}
selected_lang_name = st.selectbox("🔤 Select Language for Alerts", list(lang_name_to_code.keys()))
lang_code = lang_name_to_code[selected_lang_name]

# Train number input
train_no = st.text_input("🚄 Enter Train Number")

if st.button("Check Status & Send Alerts"):
    if not train_no.strip():
        st.error("❌ Enter a valid train number.")
    else:
        row = df[df['train_no'] == train_no.strip()]
        if row.empty:
            st.warning("🚫 Train not found in dataset.")
        else:
            row = row.iloc[0]

            # 🚨 Delay handling — simple keyword-based
            if "late" in row['status'].lower() or "delay" in row['status'].lower():
                from_station = "TPJ"  # Replace with actual origin station
                to_station = "MS"     # Replace with actual destination station
                journey_date = pd.Timestamp.now().strftime("%d-%m-%Y")
                show_alternative_link(from_station, to_station, journey_date)

            # Local link for food form
            food_link = "http://localhost:8502"

            message = f"""Train {row['train_no']}
Status: {row['status']}
Location: {row['location']}
ETA: {row['eta']}

🍽️ Fill your food preference: {food_link}
"""
            final_message = message

            # Translation
            if lang_code != 'en':
                try:
                    translated = translator.translate(message, dest=lang_code).text
                    final_message = translated
                    st.success(f"📣 Translated Message:\n\n{translated}")
                except Exception as e:
                    st.error(f"Translation Error: {e}")
            else:
                st.success(f"📣 Alert:\n\n{message}")

            # Telegram Alert
            try:
                bot = telegram.Bot(token=TELEGRAM_TOKEN)
                bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=final_message)
                st.success("✅ Telegram alert sent!")
            except Exception as e:
                st.error(f"Telegram Error: {e}")

            # Pushbullet Alert
            push_success, push_result = send_pushbullet_alert(
                PUSHBULLET_API_KEY,
                "🚨 Train Status Alert",
                final_message
            )
            if push_success:
                st.success("✅ Pushbullet notification sent!")
            else:
                st.error(f"Pushbullet Error: {push_result}")
