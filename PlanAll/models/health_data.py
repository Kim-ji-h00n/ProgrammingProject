import sqlite3

DB_PATH = 'database.db'

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # 운동 기록 테이블 생성
    c.execute("""
        CREATE TABLE IF NOT EXISTS exercise_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            exercise TEXT,
            reps INTEGER,
            sets INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()


def insert_exercise_log(exercise, reps, sets):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('INSERT INTO exercise_log (exercise, reps, sets) VALUES (?, ?, ?)',
              (exercise, reps, sets))
    conn.commit()
    conn.close()


def get_exercise_stats():
    """운동별 총 횟수/세트/횟수"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        SELECT exercise, SUM(reps), SUM(sets), COUNT(*)
        FROM exercise_log
        GROUP BY exercise
    ''')
    rows = c.fetchall()
    conn.close()

    return [
        {
            'exercise': row[0],
            'total_reps': row[1],
            'total_sets': row[2],
            'session_count': row[3]
        }
        for row in rows
    ]
