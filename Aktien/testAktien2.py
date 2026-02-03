import yfinance as yf

df = yf.download("AAPL", period="6mo")
print(df.tail())