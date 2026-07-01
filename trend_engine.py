from indicators import ema

def get_trend(df):
    ema20 = ema(df["close"], 20)
    ema50 = ema(df["close"], 50)
    ema200 = ema(df["close"], 200)

    if ema20.iloc[-1] > ema50.iloc[-1] > ema200.iloc[-1]:
        return "BULLISH"

    if ema20.iloc[-1] < ema50.iloc[-1] < ema200.iloc[-1]:
        return "BEARISH"

    return "NEUTRAL"
