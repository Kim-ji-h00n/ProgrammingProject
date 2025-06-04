import random

class ReinforcementRecommender:
    def __init__(self):
        self.history = []

    def update(self, data, feedback_score):
        # 간단한 정책 업데이트 예: 성공적인 루틴은 더 자주 추천
        self.history.append((data, feedback_score))

    def recommend(self, data):
        sleep = data['sleep']
        bpm = data['bpm']
        goal = data['goal']

        if sleep < 5 or bpm > 100:
            return f"{goal}을 위한 회복 루틴(스트레칭, 요가 등)을 추천합니다."
        if goal == "근육":
            return "고중량 웨이트 + 세트 수 증가 루틴을 추천합니다."
        elif goal == "다이어트":
            return "인터벌 러닝 + 근지구력 트레이닝을 추천합니다."
        return "전신 스트레칭 + 기초 근력 운동 추천"