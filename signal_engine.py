from trade_manager import get_trade

def score_system(trend, rsi, macd, adx, pattern, breakout):
    score = 0

    if trend != "NEUTRAL":
        score += 30

    if 40 < rsi < 60:
        score += 10

    if macd == trend:
        score += 20

    if adx > 20:
        score += 10

    if pattern != "NONE":
        score += 20

    if breakout != "NONE":
        score += 10

    return score


def generate_signal(score, trend):
    if get_trade():
        return {"signal": "BLOCKED", "score": score}

    if score >= 80:
        return {"signal": trend, "score": score}

    return {"signal": "WAIT", "score": score}
