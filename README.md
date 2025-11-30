# InvestMal AI

InvestMal AI هو روبوت تحليلي ذكي لسوق الكريبتو، يعتمد على مؤشرات RSI، MACD، و MA لاتخاذ قرارات ذكية بالشراء أو البيع.

## هيكلة المشروع

```
investmal-ai/
├── src/
│   ├── investmal_ai.py
│   ├── utils.py
│   └── api_service.py
├── api/
│   └── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## تشغيل المشروع

1. إنشاء بيئة افتراضية:

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

2. تثبيت المتطلبات:

```bash
pip install -r requirements.txt
```

3. تشغيل API:

```bash
uvicorn api.app:app --reload
```

4. الوصول إلى endpoints:

- GET /analyze?symbol=BTCUSDT
- GET /health
