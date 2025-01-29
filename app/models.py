import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS weather (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        temp REAL,
        humidity REAL,
        description TEXT
    )
""")
conn.commit()
conn.close()
