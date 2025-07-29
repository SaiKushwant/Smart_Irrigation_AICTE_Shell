import streamlit as st
import numpy as np
import joblib
model = joblib.load("FARM_IRRIGATION_SYSTEM.pkl")
st.set_page_config(page_title="Smart Sprinkler System", layout="wide")
st.markdown(
    """
    <style>
    body {
        background-color: #0f1117;
    }
    .stSlider > div[data-baseweb="slider"] > div {
        color: red;
    }
    .main-title {
        font-size: 48px;
        color: #34ebd8;
        text-align: center;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .sub-title {
        font-size: 22px;
        color: white;
        text-align: center;
        margin-bottom: 40px;
    }
    .prediction-box {
        border: 2px solid #34ebd8;
        padding: 20px;
        border-radius: 10px;
        background-color: #1c1e26;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown('<div class="main-title">💧 Smart Sprinkler System 💧</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Enter scaled sensor values (0 to 1) to predict sprinkler status</div>', unsafe_allow_html=True)
sensor_values = []
cols = st.columns(4)  # 5 sliders per row × 4 = 20

for i in range(20):
    with cols[i % 4]:
        val = st.slider(f"Sensor {i}", 0.0, 1.0, 0.5, 0.01)
        sensor_values.append(val)
if st.button("🌱 Predict Sprinklers"):
    input_array = np.array(sensor_values).reshape(1, -1)
    prediction = model.predict(input_array)[0]

    st.markdown('<div class="prediction-box">', unsafe_allow_html=True)
    st.markdown("### 🚿 Prediction Result:")
    for i, status in enumerate(prediction):
        color = "lime" if status == 1 else "red"
        st.markdown(f"<span style='color:{color}; font-size:18px;'>Sprinkler {i} (parcel_{i}): {'ON' if status == 1 else 'OFF'}</span>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
