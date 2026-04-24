import streamlit as st
import numpy as np
import os
import pickle

# Attempt to load the trained model
model_path = 'rf_model_compressed.pkl'

try:
    if not os.path.exists(model_path):
        st.error("❌ Model file not found. Please ensure 'rf_model_compressed.pkl' exists in the app directory.")
        st.stop()

    with open(model_path, 'rb') as file:
        model = pickle.load(file)

except ModuleNotFoundError as e:
    st.error("❌ Required library is missing. Try installing `scikit-learn`.")
    st.code("pip install scikit-learn")
    st.stop()

except Exception as e:
    st.error(f"❌ Failed to load model: {str(e)}")
    st.stop()

# Dictionary to map prediction to crop name
reversed_crop_dict = {
    0: 'rice', 1: 'maize', 2: 'chickpea', 3: 'kidneybeans', 4: 'pigeonpeas',
    5: 'mothbeans', 6: 'mungbean', 7: 'blackgram', 8: 'lentil', 9: 'pomegranate',
    10: 'banana', 11: 'mango', 12: 'grapes', 13: 'watermelon', 14: 'muskmelon',
    15: 'apple', 16: 'orange', 17: 'papaya', 18: 'coconut', 19: 'cotton',
    20: 'jute', 21: 'coffee'
}

# Set page configuration
st.set_page_config(page_title="Crop Recommendation System", layout="centered")

# Title
st.title("🌾 Crop Recommendation System")
st.markdown("Enter the soil and climate conditions below. Suggested ranges are based on common agricultural practices.")

# Input form
col1, col2 = st.columns(2)

with col1:
    N = st.number_input("Nitrogen (N)", min_value=0, help="Typical range: 0 - 140")
    P = st.number_input("Phosphorus (P)", min_value=0, help="Typical range: 5 - 145")
    K = st.number_input("Potassium (K)", min_value=0, help="Typical range: 5 - 205")
    ph = st.number_input("pH value", format="%.2f", help="Typical range: 3.5 - 9.5")

with col2:
    temperature = st.number_input("Temperature (°C)", help="Typical range: 8°C - 43°C")
    humidity = st.number_input("Humidity (%)", help="Typical range: 14% - 100%")
    rainfall = st.number_input("Rainfall (mm)", help="Typical range: 20 mm - 300 mm")

st.markdown("---")

# Centered wide button using columns
center_col = st.columns([1, 3, 1])[1]
with center_col:
    st.markdown("""
        <style>
        .stButton>button {
            width: 100%;
            font-size: 16px;
            padding: 10px 20px;
        }
        </style>
        """, unsafe_allow_html=True)
    predict_btn = st.button("🌱 Predict Best Crops")

# Show prediction result below
if predict_btn:
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])

    # 👉 Get probabilities
    try:
        probs = model.predict_proba(input_data)[0]

        # 👉 Top 5 crops
        top_indices = np.argsort(probs)[-5:][::-1]

        st.subheader("🌾 Top Recommended Crops")

        for i in top_indices:
            crop = reversed_crop_dict.get(i, "Unknown")
            confidence = probs[i]

            st.markdown(f"**🌱 {crop.upper()} — {confidence*100:.2f}%**")
            st.progress(float(confidence))

    except:
        # fallback if predict_proba not available
        prediction = model.predict(input_data)[0]
        crop_name = reversed_crop_dict.get(prediction, "Unknown")

        st.warning("⚠️ Showing single result (model does not support probabilities)")
        st.success(f"🌾 Recommended Crop: {crop_name.upper()}")
