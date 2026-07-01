from flask import Flask, jsonify
from data_fetcher import get_candles
from trend_engine import get_trend
from indicators import rsi, macd, atr
from support_resistance import get_support_resistance, breakout
from pattern_engine import candle_pattern
from signal_engine import score_system, generate_signal

app = Flask(__name__)

@app.route("/signal")
def signal():

    df = get_candles()
    if df is None:
        return jsonify({"error": "no data"})

    price = df["close"].iloc[-1]

    trend = get_trend(df)

    rsi_val = rsi(df["close"]).iloc[-1]
    macd_val = macd(df["close"])
    atr_val = atr(df).iloc[-1]

    support, resistance = get_support_resistance(df)
    brk = breakout(price, support, resistance)

    pattern = candle_pattern(df)

    score = score_system(trend, rsi_val, macd_val, 25, pattern, brk)

    result = generate_signal(score, trend)

    return jsonify({
        "price": price,
        "trend": trend,
        "rsi": rsi_val,
        "macd": macd_val,
        "atr": atr_val,
        "support": support,
        "resistance": resistance,
        "pattern": pattern,
        "breakout": brk,
        "score": score,
        "signal": result
    })

if __name__ == "__main__":
    app.run(debug=True)
