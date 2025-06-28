import telegram
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID

def send_telegram_alert(train_no, status, location, eta, from_station="TPJ", to_station="MS"):
    try:
        bot = telegram.Bot(token=TELEGRAM_TOKEN)

        # Create IRCTC alternate train link
        from urllib.parse import quote
        import datetime

        journey_date = datetime.datetime.now().strftime("%d-%m-%Y")
        irctc_url = (
            f"https://www.irctc.co.in/nget/train-search?"
            f"from={quote(from_station)}&to={quote(to_station)}&journeyDate={quote(journey_date)}"
        )

        # Create final message
        message = f"""🚨 Train Alert!

🚆 Train No: {train_no}
📍 Status: {status}
🗺️ Location: {location}
⏱️ ETA: {eta}

🍽️ Fill your food preference: http://localhost:8501
🔁 Book Alternate Train: {irctc_url}
"""

        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
        print("✅ Telegram alert sent!")

    except Exception as e:
        print("Telegram Error:", e)
