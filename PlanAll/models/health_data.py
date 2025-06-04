import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS health_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sleep REAL,
            bpm INTEGER,
            goal TEXT,
            exercise TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_health_data(data):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO health_data (sleep, bpm, goal, exercise) VALUES (?, ?, ?, ?)',
              (data['sleep'], data['bpm'], data['goal'], data.get('exercise')))
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

def update_latest_exercise(exercise):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('UPDATE health_data SET exercise = ? WHERE id = (SELECT MAX(id) FROM health_data)', (exercise,))
    conn.commit()
    conn.close()

#데이터 읽기
def get_all_data():
    conn = sqlite3.connect('database.db')  # 데이터베이스 연결
    c = conn.cursor()
    c.execute('SELECT * FROM health_data ORDER BY id')  # 모든 데이터 조회 (id 순서대로)
    rows = c.fetchall()  # 결과를 리스트 형태로 모두 가져오기
    conn.close()
    return rows

if __name__ == '__main__':
    all_data = get_all_data()
    for row in all_data:
        print(row)
