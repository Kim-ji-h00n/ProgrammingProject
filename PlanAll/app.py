from flask import Flask, render_template, request, redirect
from models.health_data import init_db, insert_health_data, get_latest_data
from utils.ai_engine import recommend_workout
import os

app = Flask(__name__)
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = {
            'sleep': float(request.form['sleep']),
            'bpm': int(request.form['bpm']),
            'goal': request.form['goal']
        }
        insert_health_data(data)
        return redirect('/dashboard')
    except Exception as e:
        return f"입력 처리 중 오류 발생: {e}", 400

@app.route('/dashboard')
def dashboard():
    try:
        latest = get_latest_data()
        recommendation = recommend_workout(latest)
        return render_template('dashboard.html', data=latest, recommendation=recommendation)
    except Exception as e:
        return f"추천 페이지 로딩 중 오류 발생: {e}", 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)