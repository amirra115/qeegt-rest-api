from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

@app.route("/")
def index():
    return "qEEGt REST API is running."

@app.route("/zscore", methods=["POST"])
def zscore():
    data = request.get_json()

    # Validate input
    if not data or "features" not in data or "age" not in data or "gender" not in data:
        return jsonify({"error": "Missing required fields: features, age, gender"}), 400

    features = data["features"]  # dictionary: {channel: {band: power}}
    age = data["age"]
    gender = data["gender"]

    # Simulate z-score computation by returning random values in same shape
    fake_zscores = {}
    for ch, band_powers in features.items():
        fake_zscores[ch] = {
            band: round(np.random.normal(0, 1), 2)  # normally distributed fake z-score
            for band in band_powers
        }

    return jsonify({
        "input_age": age,
        "input_gender": gender,
        "zscores": fake_zscores
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
