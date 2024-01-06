#!/usr/bin/python3
"""Defines a Flask route"""
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    """Returns a JSON response with the status OK"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'])
def get_stats():
    """Retrieve the number of each object by type"""
    model_counts = {}
    for model_name in storage.classes:
        model_counts[model_name] = storage.count(model_name)

    return jsonify(model_counts)
