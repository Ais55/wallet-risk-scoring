import json
from .compound_api import fetch_wallet_data

def extract_features(wallet_txt_path, output_json_path):
    with open(wallet_txt_path, "r") as f:
        wallet_ids = [line.strip() for line in f if line.strip()]

    features = []
    for w in wallet_ids:
        data = fetch_wallet_data(w)
        features.append(data)

    with open(output_json_path, "w") as f:
        json.dump(features, f, indent=2)

    print(f"[✓] Processed features saved to {output_json_path}")
