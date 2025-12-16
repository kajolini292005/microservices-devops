from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({
        "service": "analytics",
        "status": "UP"
    })

@app.route("/analyze")
def analyze():
    # Simulated analytics data
    return jsonify({
        "service": "Analytics Service",
        "success_rate": "92%",
        "failed_builds": 1,
        "total_builds": 12,
        "last_updated": time.ctime(),
        "alert": "None"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
