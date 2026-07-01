import pandas as pd

def get_support_resistance(df, lookback=20):
    highs = df["high"].rolling(lookback).max()
    lows = df["low"].rolling(lookback).min()

    resistance = highs.iloc[-1]
    support = lows.iloc[-1]

    return support, resistance


def breakout_check(price, support, resistance):
    if price > resistance:
        return "BREAKOUT_UP"
    elif price < support:
        return "BREAKOUT_DOWN"
    return "NO_BREAK"
