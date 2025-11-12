⚡ Electric Vehicle (EV) Price Prediction & Chatbot Assistant
🚗 A Machine Learning + Generative AI Project

This project predicts the price range of Electric Vehicles (EVs) based on their specifications such as battery capacity, top speed, acceleration, towing capacity, and seating capacity.
Additionally, it includes a Gemini-powered Chatbot that answers questions about electric vehicles, helping users understand EV technology, performance, and trends.

📆 Project Overview

| **Week**   | **Tasks Completed**                                                                                                                                                                  |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Week 1** | Problem definition, dataset collection, data cleaning, exploratory data analysis (EDA), and basic regression model setup.                                                            |
| **Week 2** | Model training with multiple algorithms (Linear Regression, Decision Tree, Random Forest), model evaluation using R², MAE, and MSE metrics, and saving the best model (`model.pkl`). |
| **Week 3** | Building an interactive Streamlit web app integrating EV price prediction with a Google Gemini chatbot assistant.                                                                    |

🎯 Problem Statement

Predict the driving range or price range of an electric vehicle based on its specifications — including battery capacity, top speed, acceleration, towing capacity, and other key performance indicators.

📊 Dataset Details

Source: Kaggle EV Cars Dataset

Key Columns:

battery → Battery capacity (kWh)

top_speed → Maximum speed (km/h)

zero_to_hundred → Acceleration (0–100 km/h in seconds)

towing_capacity_in_kg → Towing capacity (kg)

number_of_seats → Total seats

price_range → Target variable (price category in ₹ Lakhs)


🧠 Machine Learning Models Used
| Model                 | R²   | MAE   | MSE     |
| --------------------- | ---- | ----- | ------- |
| **Linear Regression** | 0.26 | 48.18 | 7737.37 |
| **Decision Tree**     | 0.54 | 35.63 | 4856.47 |
| **Random Forest**     | 0.46 | 34.95 | 5686.60 |


🧩 App Features
🔹 EV Price Predictor

-Takes EV specs as input

-Predicts estimated price range (in ₹ Lakhs) using the trained ML model

🔹 Gemini Chatbot Assistant

-Built using Google Gemini 2.5 Flash model

-Answers general queries about EVs

-Explains insights like battery efficiency, charging trends, and sustainability

🚀 Improvisations Done

-Added feature engineering (power_efficiency, performance_index, weight_factor) to improve model accuracy.

-Integrated Gemini AI chatbot for intelligent, conversational responses.

-Built a Streamlit web interface for end-to-end user interaction.

-Saved the best-performing model and automated predictions.

🏁 Results

-Best R² Score: 0.54 (Decision Tree)

-App allows both prediction and interactive chatbot conversation.

-Clean UI built with Streamlit, ready for deployment.
