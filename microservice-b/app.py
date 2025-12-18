print("### MICROSERVICE B APP.PY LOADED ###")

from flask import Flask, jsonify
import logging

app = Flask(__name__)

logging.basicConfig(
    filename="service.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

@app.route("/")
def home():
    logging.info("Home endpoint accessed")
    return "READY FOR SERVICE B"

@app.route("/health")
def health():
    logging.info("Health check called")
    return jsonify({
        "status": "UP",
        "service": "Microservice B"
    })

@app.route("/status")
def status():
    logging.info("Status endpoint accessed")
    return jsonify({
        "service": "Microservice B",
        "version": "1.0",
        "message": "Service is running normally"
    })

print(app.url_map)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
