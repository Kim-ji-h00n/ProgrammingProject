# PlanAll 프로젝트

## 주요 파일
- index.html: 웹사이트(로그인/회원가입/CSV 업로드/팀 소개)
- health_dataset.json: 샘플 건강 데이터, 새 회원 데이터 랜덤 생성에도 사용
- PlanAll.cpp: C++ 콘솔 프로그램(운동 추천/기록 저장)
- json.hpp: C++용 JSON 라이브러리

## 사용법
- 웹: index.html 실행(로컬/서버), health_dataset.csv 업로드 또는 회원가입 가능
- C++: PlanAll.cpp 컴파일 후 health_dataset.json 불러와 운동 추천 및 기록 자동 저장

## 확장
- health_dataset.json → health_dataset.csv 변환
- userdata/ 폴더에 회원별 건강 데이터 JSON 파일 자동 생성
