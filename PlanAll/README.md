# PlanAll 프로젝트

## 실행 방법
```bash
1. 의존성 설치
pip install -r requirements.txt
2. 서버 실행 
python app.py
3. (선택) 다른 기기에서 접속하고 싶다면
http://<이 컴퓨터의 IP>:5000
(Windows에서 `ipconfig`로 IP 확인)
```

## 기능
- 수면량, 심박수, 운동 목표 입력
- SQLite로 데이터 저장
- 실시간 운동 추천 로직
- 웹 기반 UI

## 확장 방향
- 스마트워치 연동
- 날씨 API로 실내/실외 추천
- 강화학습 기반 최적 루틴 추천
