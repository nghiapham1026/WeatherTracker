import requests
import sqlite3
from datetime import datetime

API_KEY = "2ba4b97a2971c2cbe37c3b4c905a51ec"
CITY = "San Francisco"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

def collect_weather_data():
    response = requests.get(URL).json()
    temp = response["main"]["temp"]
    humidity = response["main"]["humidity"]
    weather = response["weather"][0]["description"]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO weather (timestamp, temp, humidity, description) VALUES (?, ?, ?, ?)",
                   (timestamp, temp, humidity, weather))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    collect_weather_data()
