import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from proto import HealthRoutineRecommender
# 1. 데이터 로드 (CSV에 age, weight, goal, experience, preference, routine 컬럼이 있다고 가정)
df = pd.read_csv("user_data.csv")
 
 # 2. 학습/테스트 분할
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42, stratify=df['routine'])

#3. 모델 생성·학습
recommender = HealthRoutineRecommender(n_estimators=200, random_state=0)
recommender.fit(train_df)

# 4. 테스트 데이터로 예측
X_test = test_df.drop('routine', axis=1)
y_true = test_df['routine'].values
y_pred = [recommender.predict(row) for row in X_test.to_dict(orient='records')]

# 5. 성능 확인
print("Accuracy:", accuracy_score(y_true, y_pred))
print(classification_report(y_true, y_pred))
 
# 6. 모델·인코더 저장
recommender.save(model_path="model.joblib", encoders_path="encoders.joblib")

