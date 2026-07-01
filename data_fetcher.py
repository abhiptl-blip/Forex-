import requests
import pandas as pd
from config import API_KEY, BASE_URL, PAIR, TIMEFRAME

def get_candles():
    url = f"{BASE_URL}/time_series"

    params = {
        "symbol": PAIR,
        "interval": TIMEFRAME,
        "outputsize": 200,
        "apikey": API_KEY
    }

    try:
        res = requests.get(url, params=params, timeout=10)
        data = res.json()

        if "values" not in data:
            return None

        df = pd.DataFrame(data["values"])
        df = df.astype(float)
        df = df.sort_index(ascending=True)

        return df

    except:
        return None
