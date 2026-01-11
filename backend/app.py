from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app)

# load trained model
model = joblib.load("../model/personality_prediction_model.pkl")

# feature order (MUST match training)
FEATURE_ORDER = [
    "Time_spent_Alone",
    "Social_event_attendance",
    "Going_outside",
    "Friends_circle_size",
    "Post_frequency",
    "Stage_fear",
    "Drained_after_socializing"
]

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "Backend running"}), 200

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # convert input to DataFrame
        input_df = pd.DataFrame([data])[FEATURE_ORDER]

        prediction = model.predict(input_df)[0]
        probability = model.predict_proba(input_df).max()

        return jsonify({
            "prediction": prediction,
            "confidence": round(float(probability), 4)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)