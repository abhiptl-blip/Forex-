import json
import os

FILE = "active_trade.json"

def get_trade():
    if not os.path.exists(FILE):
        return None

    with open(FILE) as f:
        data = json.load(f)

    return data if data else None


def set_trade(trade):
    with open(FILE, "w") as f:
        json.dump(trade, f, indent=2)


def clear_trade():
    with open(FILE, "w") as f:
        json.dump({}, f)
