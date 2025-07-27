import json
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler

def train_and_score_model(features_path, output_path):
    # Load JSON to DataFrame
    with open(features_path, "r") as f:
        data = json.load(f)
    df = pd.DataFrame(data)

    # Features and dummy target (you can replace this with actual labels)
    X = df[['borrow_supply_ratio', 'repay_ratio', 'liquidated_count']]
    y = 1 - df['borrow_supply_ratio'] + df['repay_ratio'] - 0.2 * df['liquidated_count']

    # Train a simple random forest regressor
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    predictions = model.predict(X)

    # Normalize predictions to 0–1000
    scaler = MinMaxScaler(feature_range=(0, 1000))
    scores = scaler.fit_transform(predictions.reshape(-1, 1)).flatten()

    df['score'] = scores.astype(int)
    df[['wallet_id', 'score']].to_csv(output_path, index=False)
    print(f"Saved risk scores to: {output_path}")
