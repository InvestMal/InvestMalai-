import requests
import numpy as np
import talib

class InvestMalAI:
    def __init__(self, symbol="BTCUSDT", interval="1h", limit=300):
        self.symbol = symbol
        self.interval = interval
        self.limit = limit
        self.closes = []

    def fetch_data(self):
        url = f"https://api.binance.com/api/v3/klines?symbol={self.symbol}&interval={self.interval}&limit={self.limit}"
        resp = requests.get(url)
        resp.raise_for_status()
        self.closes = np.array([float(c[4]) for c in resp.json()])
        return self.closes

    def calculate_indicators(self):
        if not self.closes.size:
            self.fetch_data()
        closes = self.closes
        rsi = float(talib.RSI(closes, 14)[-1])
        macd, signal, _ = talib.MACD(closes)
        ma50 = float(talib.SMA(closes, 50)[-1])
        ma200 = float(talib.SMA(closes, 200)[-1])
        return {"rsi": rsi, "macd": float(macd[-1]), "signal": float(signal[-1]), "ma50": ma50, "ma200": ma200}

    def trend_detection(self, ind):
        if ind["ma50"] > ind["ma200"]:
            return "Uptrend"
        elif ind["ma50"] < ind["ma200"]:
            return "Downtrend"
        return "Sideways"

    def risk_score(self, ind):
        rsi = ind["rsi"]
        if rsi > 70:
            return "High Risk (Overbought)"
        elif rsi < 30:
            return "High Risk (Oversold)"
        elif 30 < rsi < 45:
            return "Medium Risk"
        elif 45 <= rsi <= 60:
            return "Low Risk"
        else:
            return "Medium Risk"

    def ai_recommendation(self, ind, trend):
        if trend == "Uptrend" and ind["macd"] > ind["signal"] and ind["rsi"] < 70:
            return "BUY"
        elif trend == "Downtrend" and ind["macd"] < ind["signal"] and ind["rsi"] > 30:
            return "SELL"
        return "WAIT"

    def run(self):
        ind = self.calculate_indicators()
        trend = self.trend_detection(ind)
        risk = self.risk_score(ind)
        decision = self.ai_recommendation(ind, trend)
        return {"symbol": self.symbol, "trend": trend, "risk": risk, "indicators": ind, "decision": decision}
