# Machine Learning Personality Prediction System

This project implements a machine learning–based personality prediction system developed as part of the CIS6005 – Computational Intelligence coursework.

The system predicts whether an individual is an Introvert or Extrovert based on behavioral and social attributes using supervised machine learning techniques.

## Project Components

- Machine learning model trained using Python and scikit-learn
- RESTful backend API for model inference
- Streamlit-based frontend for user interaction
- End-to-end deployment-ready pipeline

## Technologies Used

- Python
- scikit-learn
- Flask
- Streamlit
- Pandas, NumPy
- Joblib

## Endpoints Exposed

### Health Check
- GET /health

### Predict Personality
- POST /predict

#### Sample JSON Input
{
  "Time_spent_Alone": 4,
  "Social_event_attendance": 3,
  "Going_outside": 2,
  "Friends_circle_size": 5,
  "Post_frequency": 2,
  "Stage_fear": 1,
  "Drained_after_socializing": 1
}


## Disclaimer

This project is developed for academic purposes.

Designed and Developed by Dasindu Hewagamage.