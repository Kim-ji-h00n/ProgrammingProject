from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    mood = data['mood']
    calories = data['calories']
    sleep = data['sleepMinutes']

    if sleep < 360 or mood.lower() in ['tired', 'sad']:
        routine = "가벼운 스트레칭"
        duration = 10
    elif calories > 800:
        routine = "유산소 중심 루틴"
        duration = 30
    else:
        routine = "균형 잡힌 전신 루틴"
        duration = 20

    return jsonify(recommendation=routine, duration=duration)

if __name__ == '__main__':
    app.run(debug=True)
