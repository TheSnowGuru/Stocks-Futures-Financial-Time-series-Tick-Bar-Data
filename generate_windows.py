ohlcv = {
    k: v.vbt.split_into_ranges(range_len=window_len.days, n=window_count) 
    for k, v in ohlcv.items()
}
    
print(ohlcv['Open'].shape)
