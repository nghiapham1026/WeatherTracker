import pandas as pd
import sqlite3

def analyze_weather():
    conn = sqlite3.connect("database.db")
    df = pd.read_sql_query("SELECT * FROM weather", conn)
    avg_temp = df["temp"].mean()
    avg_humidity = df["humidity"].mean()
    conn.close()
    return f"Avg Temp: {avg_temp:.2f}°C, Avg Humidity: {avg_humidity:.2f}%"

if __name__ == "__main__":
    print(analyze_weather())
