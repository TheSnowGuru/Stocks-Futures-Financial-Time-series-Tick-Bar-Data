entries = pd.DataFrame.vbt.signals.empty_like(ohlcv['Open'])
entries.iloc[0, :] = True

print(entries.shape)
