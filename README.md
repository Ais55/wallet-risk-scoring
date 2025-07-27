# Wallet Risk Scoring using Compound V2

## Methodology

1. **Data Collection**  
   Used Compound V2 subgraph to fetch supply, borrow, repay, and liquidation events.

2. **Feature Engineering**  
   Extracted:
   - Total borrowed, supplied, repaid
   - Borrow/Supply Ratio
   - Repay/Borrow Ratio
   - Liquidation count

3. **Scoring Logic**
   - Normalized key metrics
   - Weighted scoring:
     - Borrow/Supply Ratio (30%)
     - Repay Ratio (30%)
     - Liquidation Count (40%)

4. **Output**
   - Score range: 0 (high risk) to 1000 (low risk)

4. **How to RUN**
   *clone github
      git clone https://github.com/Ais55/wallet-risk-scoring.git
      cd wallet_risk_scoring

   *Create a virtual environment (optional but recommended)on terminal
      python -m venv .venv
      source .venv/bin/activate     # On Linux/macOS
      .venv\Scripts\activate        # On Windows

   *Install required packages
      pip install -r requirements.txt on terminal
   
   *Run the main script
      python main.py on terminal





