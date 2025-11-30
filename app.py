from fastapi import FastAPI, Query
from src.investmal_ai import InvestMalAI

app = FastAPI(title="InvestMal AI API")

@app.get("/analyze")
def analyze(symbol: str = Query("BTCUSDT", max_length=10)):
    bot = InvestMalAI(symbol=symbol)
    return bot.run()

@app.get("/health")
def health():
    return {"status": "ok"}
