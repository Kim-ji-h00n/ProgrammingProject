from flask import Flask, render_template, request, redirect
from models.health_data import init_db, insert_health_data, get_latest_data, update_latest_exercise
from utils.ai_engine import recommend_workout

app = Flask(__name__)
init_db()

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/start')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = {
        'sleep': float(request.form['sleep']),
        'bpm': int(request.form['bpm']),
        'goal': request.form['goal']
    }
    insert_health_data(data)
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    latest = get_latest_data()
    recommendation = recommend_workout(latest)
    return render_template('dashboard.html', data=latest, recommendation=recommendation)

@app.route('/choose_exercise', methods=['POST'])
def choose_exercise():
    selected_exercise = request.form['exercise']
    
    update_latest_exercise(selected_exercise)

    return render_template('exercise.html', exercise=selected_exercise)

if __name__ == '__main__':
    app.run(debug=True)
