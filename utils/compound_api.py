import random

def fetch_wallet_data(wallet_id):
    supply_total = round(random.uniform(100, 2000), 2)
    borrow_total = round(random.uniform(0, supply_total), 2)
    repay_total = round(random.uniform(0, borrow_total), 2)
    liquidated_count = random.randint(0, 3)

    borrow_supply_ratio = borrow_total / supply_total if supply_total else 0
    repay_ratio = repay_total / borrow_total if borrow_total else 0

    return {
        "wallet_id": wallet_id,
        "borrow_total": borrow_total,
        "supply_total": supply_total,
        "repay_total": repay_total,
        "borrow_supply_ratio": borrow_supply_ratio,
        "repay_ratio": repay_ratio,
        "liquidated_count": liquidated_count
    }
