from flask import Flask, render_template, request, redirect
from models.health_data import init_db, insert_exercise_log, get_exercise_stats

app = Flask(__name__)
init_db()

@app.route('/')
def main():
    return render_template('main.html')


@app.route('/dashboard')
def dashboard():
    # 추천 운동은 외부에서 수행한다고 가정
    return render_template('select.html')


@app.route('/choose_exercise', methods=['POST'])
def choose_exercise():
    selected_exercise = request.form['exercise']
    return render_template('exercise.html', exercise=selected_exercise)


@app.route('/exercise_log', methods=['POST'])
def exercise_log():
    exercise_name = request.form['exercise']
    reps = int(request.form['reps'])
    sets = int(request.form['sets'])

    insert_exercise_log(exercise_name, reps, sets)
    return redirect('/')


@app.route('/exercise_stats')
def exercise_stats():
    stats = get_exercise_stats()
    return render_template('exercise_stats.html', stats=stats)


if __name__ == '__main__':
    app.run(debug=True)
