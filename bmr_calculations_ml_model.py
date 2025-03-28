# -*- coding: utf-8 -*-
"""Bmr_calculations.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IqPcrSl7o56u1IFLu0kJqhAY5XIA0Gge
"""

import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load dataset
df = pd.read_csv("/content/drive/MyDrive/nazika/BMR_Dataset.csv")

# Drop 'user_id' column if not needed
df = df.drop(columns=["user_id"], errors='ignore')

# Encode categorical feature (Gender)
label_encoder = LabelEncoder()
df['gender'] = label_encoder.fit_transform(df['gender'])  # Male = 1, Female = 0

# Define features (X) and target variable (y)
X = df.drop(columns=["BMR"])
y = df["BMR"]

# Train-Test Split (80-20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train Random Forest Regressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, "bmr_random_forest_model.pkl")
print("Model saved successfully as 'bmr_random_forest_model.pkl'")

# Predictions
y_pred = model.predict(X_test)

# Model Evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"Model Evaluation:\nMAE: {mae}\nMSE: {mse}\nRMSE: {rmse}\nR² Score: {r2}")

# Example Prediction for a New User
new_user_df = pd.DataFrame([[28, 77.73, 179.49, 0]], columns=X.columns)
bmr_prediction = model.predict(new_user_df)
print(f"Predicted BMR: {bmr_prediction[0]:.2f}")

