import json

FILE = "history.json"

def save_history(trade):
    try:
        with open(FILE) as f:
            data = json.load(f)
    except:
        data = []

    data.append(trade)

    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)
