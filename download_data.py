cols = ['Open', 'Low', 'High', 'Close', 'Volume']
ohlcv_by_symbol = vbt.utils.data.download(symbols, start=start_date, end=end_date, cols=cols)

print(ohlcv_by_symbol.keys())
print(ohlcv_by_symbol['BTC-USD'].shape)
