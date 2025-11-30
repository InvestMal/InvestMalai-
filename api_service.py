import requests

def get_price(symbol="BTCUSDT"):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    resp = requests.get(url)
    resp.raise_for_status()
    return float(resp.json()["price"])
