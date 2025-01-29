from flask import Blueprint, render_template, jsonify
import sqlite3

weather_bp = Blueprint("weather", __name__)

@weather_bp.route("/")
def home():
    return render_template("index.html")

@weather_bp.route("/weather", methods=["GET"])
def get_weather():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM weather ORDER BY timestamp DESC LIMIT 10")
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)
