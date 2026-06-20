import streamlit as st
from sensors import get_sensor_data
from ai_module import detect_obstacle, detect_emergency
from navigation import choose_path

st.title("🚁 Response Drone Control Panel")

st.write("AI Drone System (GitHub Safe Version)")

if st.button("Start Drone Simulation"):

    data = get_sensor_data()

    st.subheader("📡 Sensor Data")
    st.write(data)

    st.subheader("🤖 AI Detection")

    st.write(detect_obstacle(data["obstacle"]))
    st.write(detect_emergency(data["smoke_level"]))

    st.subheader("🧭 Navigation Decision")

    result = choose_path(12, 3, data["signal_strength"])
    st.success(result)