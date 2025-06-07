def recommend_workout(data):
    sleep = data['sleep']
    bpm = data['bpm']
    goal = data['goal']

    if sleep < 5 or bpm > 100:
        return f"{goal}을 위한 가벼운 운동(스트레칭, 요가 등)을 추천합니다."
    elif goal == "근육":
        return "고강도 웨이트 트레이닝 루틴을 추천합니다. " \
        "도구를 사용할 수 있다면 턱걸이, 벤치프레스 등을, " \
        "그렇지 않으면 푸쉬업이나 스쿼트는 어떨까요?"
    elif goal == "다이어트":
        return "유산소 운동 + 근지구력 루틴을 추천합니다."
    return "기본 스트레칭 + 코어 운동을 추천합니다."
