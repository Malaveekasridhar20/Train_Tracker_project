import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="🍽️ Food Preference Form")

st.title("🍽️ Train Food Preference Form")
st.markdown("Please let us know your food requirements for your train journey.")

# Form fields
name = st.text_input("👤 Your Name")
train_no = st.text_input("🚆 Train Number")
travel_date = st.date_input("📅 Travel Date")
want_food = st.radio("🍴 Do you want food during the journey?", ["Yes", "No"])

food_type = None
special_instructions = ""

if want_food == "Yes":
    food_type = st.selectbox("🍽️ Food Type", ["Veg", "Non-Veg", "Jain", "Other"])
    special_instructions = st.text_area("📝 Any special instructions? (Optional)")

if st.button("Submit"):
    if not name or not train_no:
        st.warning("Please fill in all required fields.")
    else:
        # Create record
        data = {
            "name": name,
            "train_no": train_no,
            "travel_date": str(travel_date),
            "want_food": want_food,
            "food_type": food_type if want_food == "Yes" else "Not Required",
            "special_instructions": special_instructions if want_food == "Yes" else "",
            "submitted_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        # Save to CSV
        df = pd.DataFrame([data])
        csv_path = "data/food_preferences.csv"

        try:
            existing = pd.read_csv(csv_path)
            df.to_csv(csv_path, mode='a', header=False, index=False)
        except FileNotFoundError:
            df.to_csv(csv_path, index=False)

        st.success("✅ Your food preference has been recorded!")
