from utils.feature_utils import extract_features
from utils.model_utils import train_model, predict_scores

def main():
    wallet_file = "data/wallets.txt"
    feature_json = "data/processed_features.json"
    output_csv = "output/risk_scores.csv"

    print("➡️ Extracting wallet features")
    extract_features(wallet_file, feature_json)

    print("➡️ Training random forest model")
    train_model(feature_json)

    print("➡️ Predicting risk scores")
    predict_scores(feature_json, output_csv)

    print(f"✅ All done! Risk scores saved at {output_csv}")

if __name__ == "__main__":
    main()
