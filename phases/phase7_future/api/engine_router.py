from flask import Blueprint, jsonify, request
from datetime import datetime

api_blueprint = Blueprint("api", __name__)

@api_blueprint.route("/ping", methods=["GET"])
def ping():
    return jsonify({"status": "alive", "timestamp": datetime.utcnow().isoformat()})

@api_blueprint.route("/prompt/score", methods=["POST"])
def prompt_score():
    data = request.get_json()
    prompt = data.get("prompt", "")
    score = len(prompt.split()) / 10.0
    return jsonify({"prompt": prompt, "score": round(min(score, 1.0), 3)})

@api_blueprint.route("/generate/report", methods=["GET"])
def generate_report():
    return jsonify({
        "report": "Synthèse du moteur ABACABA",
        "timestamp": datetime.utcnow().isoformat()
    })
