def candlestick_signal(df):
    last = df.iloc[-1]
    prev = df.iloc[-2]

    body = abs(last["close"] - last["open"])
    range_ = last["high"] - last["low"]

    # Bullish Engulfing
    if last["close"] > last["open"] and prev["close"] < prev["open"]:
        if body > (range_ * 0.6):
            return "BULLISH_ENGULFING"

    # Bearish Engulfing
    if last["close"] < last["open"] and prev["close"] > prev["open"]:
        if body > (range_ * 0.6):
            return "BEARISH_ENGULFING"

    # Pin bar (simple)
    if (range_ > 0) and (body < range_ * 0.3):
        return "PIN_BAR"

    return "NONE"
