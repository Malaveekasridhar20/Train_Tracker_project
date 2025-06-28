# 🚆 Train Tracker & Alert System

This project provides a real-time train tracking system with Telegram alerts and offline fallback mode using datasets.

## Features
- Streamlit Web App for user input
- Telegram Bot for real-time alerts
- Offline support using `train_status_data.csv`
- Easy deployment

## Setup
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set your Telegram Bot token and chat ID in `config.py`

3. Run the app:
```bash
streamlit run app.py
```

## Dataset Format
`data/train_status_data.csv`:
```
train_no,status,location,eta
12623,15 min delay,Trichy Jn,10:30 AM
...
```
