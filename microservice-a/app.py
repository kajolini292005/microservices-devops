import requests

from flask import Flask, jsonify
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


app = Flask(__name__)

@app.route("/")
def home():
    return "Hello!!! READY FOR SERVICE A!!..."

@app.route("/health")
def health():
    return jsonify({
        "status": "UP",
        "service": "Microservice A"
    })

@app.route("/status")
def status():
    return jsonify({
        "service": "Microservice A",
        "version": "1.0",
        "message": "Service is running normally"
    })

@app.route("/call-b")
def call_service_b():
    app.logger.info("Service A attempting to call Service B")
    try:
        response = requests.get("http://microservice-b:5001/status", timeout=3)

        app.logger.info("Service B responded successfully")
        return {
            "service": "A",
            "called_service": "B",
            "response_from_b": response.json()
        }
    except Exception as e:
        app.logger.error("Service B call failed")
        return {
            "service": "A",
            "error": "Service B not reachable",
            "details": str(e)
        }, 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
