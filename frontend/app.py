import streamlit as st
import requests

# --------------------------------------------------
# App configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Personality Prediction System",
    layout="centered"
)

st.title("Personality Prediction System")
st.write(
    "This application predicts whether an individual is an **Introvert** or "
    "**Extrovert** based on behavioral and social attributes."
)

# --------------------------------------------------
# Input form
# --------------------------------------------------
st.header("Enter Behavioral Information")

time_spent_alone = st.slider(
    "Time Spent Alone",
    min_value=0,
    max_value=10,
    value=5
)

social_event_attendance = st.slider(
    "Social Event Attendance",
    min_value=0,
    max_value=10,
    value=5
)

going_outside = st.slider(
    "Frequency of Going Outside",
    min_value=0,
    max_value=10,
    value=5
)

friends_circle_size = st.slider(
    "Friends Circle Size",
    min_value=0,
    max_value=15,
    value=5
)

post_frequency = st.slider(
    "Social Media Post Frequency",
    min_value=0,
    max_value=10,
    value=5
)

stage_fear = st.selectbox(
    "Do you experience stage fear?",
    options=["No", "Yes"]
)

drained_after_socializing = st.selectbox(
    "Do you feel drained after socializing?",
    options=["No", "Yes"]
)

# --------------------------------------------------
# Prepare request payload
# --------------------------------------------------
payload = {
    "Time_spent_Alone": time_spent_alone,
    "Social_event_attendance": social_event_attendance,
    "Going_outside": going_outside,
    "Friends_circle_size": friends_circle_size,
    "Post_frequency": post_frequency,
    "Stage_fear": 1 if stage_fear == "Yes" else 0,
    "Drained_after_socializing": 1 if drained_after_socializing == "Yes" else 0
}

# --------------------------------------------------
# Prediction trigger
# --------------------------------------------------
if st.button("Predict Personality"):
    try:
        response = requests.post(
            "http://127.0.0.1:5000/predict",
            json=payload
        )

        if response.status_code == 200:
            result = response.json()

            st.subheader("Prediction Result")
            st.success(f"Personality: **{result['prediction']}**")
            st.info(f"Confidence: **{result['confidence']}**")

        else:
            st.error("Prediction failed. Please check the backend.")

    except Exception as e:
        st.error(f"Error connecting to backend: {e}")

st.write("****")     
st.write("**@2026 Designed and Developed by Dasindu Hewagamage.**")        
