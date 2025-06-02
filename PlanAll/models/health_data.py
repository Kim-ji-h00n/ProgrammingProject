import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS health_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sleep REAL,
            bpm INTEGER,
            goal TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_health_data(data):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO health_data (sleep, bpm, goal) VALUES (?, ?, ?)',
              (data['sleep'], data['bpm'], data['goal']))
    conn.commit()
    conn.close()

def get_latest_data():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT sleep, bpm, goal FROM health_data ORDER BY id DESC LIMIT 1')
    row = c.fetchone()
    conn.close()
    return {'sleep': row[0], 'bpm': row[1], 'goal': row[2]}

def get_recent_stats(limit=5):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT sleep, bpm FROM health_data ORDER BY id DESC LIMIT ?', (limit,))
    rows = c.fetchall()
    conn.close()

    labels = [f"{i+1}일 전" for i in range(len(rows))][::-1]
    sleep = [r[0] for r in rows][::-1]
    bpm = [r[1] for r in rows][::-1]
    return {'labels': labels, 'sleep': sleep, 'bpm': bpm}
