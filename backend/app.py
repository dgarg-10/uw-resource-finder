from flask import Flask, jsonify, request
from flask_cors import CORS
from recommend import get_recommendation
from db import (
    get_all_resources,
    get_resource_by_id,
    get_hours_for_resource,
    get_hours_for_day,
    get_open_now,
    search_resources,
    get_favorites,
    add_favorite,
    remove_favorite
)
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import sentry_sdk
import os
import logging

sentry_sdk.init(
    dsn=os.environ.get("SENTRY_DSN"),
    traces_sample_rate=0.2,
    send_default_pii=False,
)

logger = logging.getLogger(__name__)


app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": [
    "http://localhost:5174",
    "https://uw-resource-finder-virid.vercel.app",
    "https://uw-resources.vercel.app"
]}})

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["100 per minute"],
    storage_uri="memory://"
)

@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify({"error": "Too many requests. Please wait a moment and try again."}), 429

@app.route("/api/resources", methods=["GET"])
def list_resources():
    return jsonify(get_all_resources())

@app.route("/api/resources/search", methods=["GET"])
def search():
    query = request.args.get("q", "")
    if not query:
        return jsonify([])
    results = search_resources(query)
    return jsonify(results)

@app.route("/api/resources/open", methods=["GET"])
def open_now():
    return jsonify(get_open_now())

@app.route("/api/hours/today", methods=["GET"])
def today_hours():
    return jsonify(get_hours_for_day())


@app.route("/api/resources/<int:resource_id>", methods=["GET"])
def get_resource(resource_id):
    resource = get_resource_by_id(resource_id)
    if resource is None:
        return jsonify({"error": "Resource not found"}), 404    #returns 404 status code which can be checked by the frontend
    return jsonify(resource)

@app.route("/api/resources/<int:resource_id>/hours", methods=["GET"])
def resource_hours(resource_id):
    return jsonify(get_hours_for_resource(resource_id))


@app.route("/api/favorites", methods=["POST"])
def add_fav():
    data = request.get_json()   #parses the JSON body sent by the frontend
    user_id = data["user_id"]
    resource_id = data["resource_id"]
    add_favorite(user_id, resource_id)
    return jsonify({"status": "added"}), 201

@app.route("/api/favorites", methods=["DELETE"])
def remove_fav():
    data = request.get_json()
    user_id = data["user_id"]
    resource_id = data["resource_id"]
    remove_favorite(user_id, resource_id)
    return jsonify({"status": "removed"})

@app.route("/api/favorites/<user_id>", methods=["GET"])
def list_favorites(user_id):
    return jsonify(get_favorites(user_id))

@app.route("/api/recommend", methods=["POST"])
@limiter.limit("10 per minute")
def recommend():
    data = request.get_json()
    query = data.get("query", "")
    if not query:
        return jsonify({"error": "No query provided"}), 400

    try:
        recommendation = get_recommendation(query)
        return jsonify({"recommendation": recommendation})
    except Exception as e:
        logger.error(f"Recommendation failed: {e}", exc_info=True)
        return jsonify({"error": "Failed to get recommendation"}), 500




if __name__ == "__main__":
    app.run(debug=True, port=5001)