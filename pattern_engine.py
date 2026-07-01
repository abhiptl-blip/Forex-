def candle_pattern(df):
    last = df.iloc[-1]
    prev = df.iloc[-2]

    body = abs(last["close"] - last["open"])
    range_ = last["high"] - last["low"]

    if last["close"] > last["open"] and prev["close"] < prev["open"]:
        if body > range_ * 0.6:
            return "BULLISH_ENGULFING"

    if last["close"] < last["open"] and prev["close"] > prev["open"]:
        if body > range_ * 0.6:
            return "BEARISH_ENGULFING"

    if body < range_ * 0.3:
        return "PIN_BAR"

    return "NONE"
