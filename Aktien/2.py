import yfinance as yf
import time

#df_ = yf.download('AAPL',start='01.01.2024')

for element in [1,2,3,4,5,6,7,8,9,10]:

    stock = yf.Ticker("MSFT")

    historicalData = stock.history(period="1d")
    closing_prices = historicalData["Open"]
    currentPrice = closing_prices.iloc[-1]

    #print(historicalData)
    #print(closing_prices)
    print(currentPrice)
    time.sleep(10)
print("Finish")