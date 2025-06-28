import pandas as pd
from googletrans import Translator
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID
import telegram

def get_train_status(train_no):
    df = pd.read_csv("data/train_status_data.csv")
    df['train_no'] = df['train_no'].astype(str)
    row = df[df['train_no'] == str(train_no)]
    if row.empty:
        return None
    row = row.iloc[0]
    return {
        "train_no": row['train_no'],
        "status": row['status'],
        "location": row['location'],
        "eta": row['eta']
    }

def translate_message(message, lang_code):
    translator = Translator()
    translated = translator.translate(message, dest=lang_code)
    return translated.text

def send_telegram_message(message):
    try:
        bot = telegram.Bot(token=TELEGRAM_TOKEN)
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
    except Exception as e:
        print("Telegram Error:", e)

def notify_train_status(train_no, lang='en'):
    data = get_train_status(train_no)
    if not data:
        print("Train not found.")
        return

    message = f"""Train {data['train_no']}
Status: {data['status']}
Location: {data['location']}
ETA: {data['eta']}"""

    if lang != 'en':
        translated = translate_message(message, lang)
        print(f"\n🔁 Translated Message ({lang}):\n", translated)
        send_telegram_message(translated)
    else:
        print(f"\n✅ English Message:\n{message}")
        send_telegram_message(message)

# Example usage:
notify_train_status(12770, lang='ta')  # Tamil
