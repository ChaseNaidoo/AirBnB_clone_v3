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
    classes = {"Amenity": 0, "City": 0, "Place": 0, "Review": 0, "State": 0, "User": 0}

    for class_name in classes:
        count = storage.count(class_name)
        classes[class_name] = count

    return jsonify(classes)
