from flask import Flask, jsonify, render_template
import requests
import logging
import time

app = Flask(__name__)

SERVICE_B_URL = "http://localhost:5001/analyze"


logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

@app.route("/")
def dashboard():
    logging.info("Dashboard accessed")
    return render_template("index.html")

@app.route("/health")
def health():
    return jsonify({
        "service": "dashboard",
        "status": "UP",
        "time": time.ctime()
    })

@app.route("/status")
def status():
    logging.info("Status API called")

    analytics = {"message": "Service B not connected"}
    try:
        analytics = requests.get(SERVICE_B_URL, timeout=2).json()
    except Exception as e:
        logging.error(f"Analytics service error: {e}")

    return jsonify({
        "build_status": "SUCCESS",
        "deployment_status": "COMPLETED",
        "last_deployed": time.ctime(),
        "analytics": analytics
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
