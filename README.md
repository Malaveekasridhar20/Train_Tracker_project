# 🚆 Train Tracker – Real-Time Train Monitoring & Alerts System

**Train Tracker** is a real-time Indian Railways monitoring and notification system built with **Python**, **Streamlit**, and **Telegram Bot API**. It enables users to receive live updates about train locations, fill in food preferences, and get multilingual alerts via Telegram — all in one place.

---

## 📌 Features

- 📍 **Live Train Location Tracker**  
- 🔔 **Real-Time Alerts** via **Telegram Bot** (no paid SMS required)  
- 🌐 **Multilingual Support** for user alerts  
- 🍱 **Food Preference Form** integrated with train schedule  
- 📊 **Simple and Clean UI** using **Streamlit**  
- 🧠 Supports **Offline Mode** using preloaded train status data  
- 🗃️ Built-in **SQLite** database for managing subscriptions

---

## 🛠️ Tech Stack

- **Frontend/UI**: Streamlit  
- **Backend**: Python  
- **Database**: SQLite  
- **Alerting System**: Telegram Bot API, Pushbullet  
- **Language Handling**: Google Translate API / Language Packs  
- **Data Source**: Offline CSV + Planned Live API Support

---

## 📂 Project Structure
train_tracker_project/
│
├── app.py                      # Main Streamlit app
├── bot.py                      # Telegram bot handler
├── config.py                   # Configuration for API tokens & paths
├── food_form.py                # Streamlit food preference form
├── multilingual_alert.py       # Language-based alerting logic
├── pushbullet_alert.py         # Sends alerts via Pushbullet
├── send_telegram_alert.py      # Sends alerts via Telegram
│
├── data/
│   ├── food_preferences.csv
│   └── train_status_data.csv
│
├── utils/
│   └── offline_data_loader.py
│
├── requirements.txt
└── README.md



---

## 🚀 Getting Started
### 1. Clone the Repository
git clone https://github.com/Malaveekasridhar20/Train_Tracker_project.git
cd Train_Tracker_project

### 2. Create Virtual Environment (Optional but Recommended)
python -m venv venv
venv\Scripts\activate  # For Windows
or
source venv/bin/activate  # For Linux/Mac

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Configure Telegram Bot
Edit the config.py file and fill in your credentials:
TELEGRAM_TOKEN = "your_bot_token"
TELEGRAM_CHAT_ID = "your_chat_id"

### 5. Run the Streamlit App
streamlit run app.py
