import telegram
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID

def send_telegram_alert(message):
    try:
        bot = telegram.Bot(token=TELEGRAM_TOKEN)
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=🍽️ Fill your food preference: http://localhost:8501)
    except Exception as e:
        print("Telegram Error:", e)
