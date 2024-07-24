import yfinance, json

symbol = 'MSF.DE'
microsoft = yfinance.Ticker(symbol)
daten = microsoft.info
#print(json.dumps(daten, indent=4))
#print(daten['currentPrice'])
history = microsoft.history(period = '1mo', interval = '1d')['Open']
for prize in history:
    print(prize)
#print(microsoft.history_metadata)
