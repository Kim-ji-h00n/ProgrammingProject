
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

class HealthRoutineRecommender:
    def __init__(self, n_estimators=100, random_state=42):
        self.model = RandomForestClassifier(n_estimators=n_estimators, random_state=random_state)
        self.label_encoders = {}

    def fit(self, df, feature_cols=None, target_col='routine'):
        """
        df: pandas DataFrame containing features and target.
        feature_cols: list of feature column names. If None, use all columns except target_col.
        """
        if feature_cols is None:
            feature_cols = [c for c in df.columns if c != target_col]
        # Encode categorical columns
        for col in feature_cols + [target_col]:
            if df[col].dtype == 'object' or col == target_col:
                le = LabelEncoder()
                df[col] = le.fit_transform(df[col])
                self.label_encoders[col] = le
        X = df[feature_cols]
        y = df[target_col]
        self.model.fit(X, y)

    def predict(self, user_data):
        """
        user_data: dict with the same keys as the feature columns before encoding.
        Returns the predicted routine as original label.
        """
        df = pd.DataFrame([user_data])
        for col, le in self.label_encoders.items():
            if col in df.columns:
                df[col] = le.transform(df[col])
        feature_cols = [c for c in df.columns if c != 'routine']
        pred = self.model.predict(df[feature_cols])
        return self.label_encoders['routine'].inverse_transform(pred)[0]

    def save(self, model_path='model.joblib', encoders_path='encoders.joblib'):
        joblib.dump(self.model, model_path)
        joblib.dump(self.label_encoders, encoders_path)
        
    def load(self, model_path='model.joblib', encoders_path='encoders.joblib'):
        self.model = joblib.load(model_path)
        self.label_encoders = joblib.load(encoders_path)
        
    if __name__ == "__main__":
         data = {
             'age': [25, 35, 29, 40, 22, 31],
             'weight': [70, 85, 65, 90, 60, 75],
             'goal': ['muscle_gain', 'fat_loss', 'maintenance', 'fat_loss', 'muscle_gain', 'maintenance'],
             'experience': ['beginner', 'advanced', 'intermediate', 'advanced', 'beginner', 'intermediate'],
             'preference': ['weights', 'cardio', 'mixed', 'cardio', 'weights', 'mixed'],
             'routine': ['bulk_up', 'cutting', 'hybrid', 'cutting', 'bulk_up', 'hybrid']
             }
         df = pd.DataFrame(data)
 
         # 모델 학습 및 저장
         recommender = HealthRoutineRecommender()
         recommender.fit(df)
         recommender.save()
     
         # 새로운 사용자 예측
         new_user = {
             'age': 28,
             'weight': 68,
             'goal': 'muscle_gain',
             'experience': 'beginner',
             'preference': 'weights'
         }
         print("✅ 추천 루틴:", recommender.predict(new_user))
