def get_support_resistance(df, lookback=20):
    support = df["low"].rolling(lookback).min().iloc[-1]
    resistance = df["high"].rolling(lookback).max().iloc[-1]
    return support, resistance


def breakout(price, support, resistance):
    if price > resistance:
        return "BREAKOUT_UP"
    if price < support:
        return "BREAKOUT_DOWN"
    return "NONE"
