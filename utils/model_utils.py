import json
import numpy as np
import os
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib

def train_model(features_json_path):
    df = pd.read_json(features_json_path)

    # Simulate target score if actual labels missing
    df['score'] = (
        (1 - df['borrow_supply_ratio']) * 0.3 +
        df['repay_ratio'] * 0.3 +
        (1 - df['liquidated_count'] / (df['liquidated_count'].max() + 1e-5)) * 0.4
    ) * 1000
    df['score'] = df['score'].astype(int)

    X = df[['borrow_supply_ratio', 'repay_ratio', 'liquidated_count']]
    y = df['score']

    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    mse = mean_squared_error(y_test, preds)
    print(f"Model training done – MSE on test set: {mse:.2f}")

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/risk_model.pkl")
    joblib.dump(scaler, "models/scaler.pkl")
    print("[✓] Model and scaler saved under 'models/' folder.")

def predict_scores(features_json_path, output_csv_path):
    df = pd.read_json(features_json_path)
    X = df[['borrow_supply_ratio', 'repay_ratio', 'liquidated_count']]

    model = joblib.load("models/risk_model.pkl")
    scaler = joblib.load("models/scaler.pkl")
    X_scaled = scaler.transform(X)

    df['score'] = model.predict(X_scaled).astype(int)
    df[['wallet_id', 'score']].to_csv(output_csv_path, index=False)
    print(f"[✓] Risk scores saved to {output_csv_path}")
