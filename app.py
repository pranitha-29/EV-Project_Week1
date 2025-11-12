import streamlit as st
import pandas as pd
import joblib
import google.generativeai as genai

st.set_page_config(page_title="EV Price Predictor & Chatbot", page_icon="⚡", layout="centered")

# Load your trained model
@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

model = load_model()



st.title("⚡ Electric Vehicle Price Range Prediction")
st.write("Enter the EV specifications below to predict its estimated price range.")

battery = st.number_input("🔋 Battery Capacity (kWh)", min_value=20.0, max_value=200.0, step=1.0)
top_speed = st.number_input("🚗 Top Speed (km/h)", min_value=80, max_value=400, step=5)
acceleration = st.number_input("⏱ 0–100 km/h Acceleration (sec)", min_value=1.0, max_value=20.0, step=0.1)
towing_capacity = st.number_input("🛻 Towing Capacity (kg)", min_value=0, max_value=5000, step=100)
seats = st.slider("💺 Number of Seats", min_value=2, max_value=8, value=5)

if st.button("🔮 Predict Price Range"):
    input_df = pd.DataFrame({
        "battery": [battery],
        "top_speed": [top_speed],
        "zero_to_hundred": [acceleration],
        "towing_capacity_in_kg": [towing_capacity],
        "number_of_seats": [seats]
    })
    input_df["power_efficiency"] = input_df["battery"] / input_df["top_speed"]
    input_df["performance_index"] = input_df["top_speed"] / input_df["zero_to_hundred"]
    input_df["weight_factor"] = input_df["towing_capacity_in_kg"] / input_df["number_of_seats"]

    prediction = model.predict(input_df)[0]
    st.success(f"💰 Predicted EV Price Range: **₹{round(prediction, 2)} Lakhs**")

st.markdown("---")



# 🤖 Chatbot Section (Google Gemini)

try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
except Exception as e:
    st.error("⚠️ Google API key not found. Please add it in .streamlit/secrets.toml file.")
    st.stop()

# ✅ Use the latest supported model
MODEL_NAME = "models/gemini-2.5-flash"   # ← This is the correct model from your list

st.header("🤖 Electric Vehicle Chatbot Assistant")
st.write("Ask me anything about Electric Vehicles — performance, range, or sustainability!")

user_query = st.text_input("💬 Type your question here:")

if user_query:
    with st.spinner("Thinking..."):
        try:
            model_chat = genai.GenerativeModel(MODEL_NAME)
            response = model_chat.generate_content(user_query)
            st.write("**Assistant:**", response.text)
        except Exception as e:
            st.error(f"❌ Error: {e}")


st.markdown("---")
st.caption("Developed by Pranitha D | EV Price Prediction Project 2025")
