import vectorbt as vbt

import numpy as np
import pandas as pd
import itertools
from datetime import datetime, timedelta
from numba import njit
import ipywidgets

seed = 42
symbols = [
    'BTC-USD', 'ETH-USD', 'XRP-USD', 'BCH-USD', 'LTC-USD', 
    'BNB-USD', 'EOS-USD', 'XLM-USD', 'XMR-USD', 'ADA-USD'
]
start_date = datetime(2018, 1, 1)
end_date = datetime(2021, 1, 1)
time_delta = end_date - start_date
window_len = timedelta(days=180)
window_count = 400
exit_types = ['SL', 'TS', 'TP', 'Random', 'Holding']
step = 0.01  # in %
stops = np.arange(step, 1 + step, step)

vbt.settings.layout['template'] = vbt.settings.dark_template

vbt.settings.portfolio['freq'] = '1D'
vbt.settings.portfolio['init_cash'] = 100. # in $
vbt.settings.portfolio['fees'] = 0.0025 # in %
vbt.settings.portfolio['slippage'] = 0.0025 # in %

print(pd.Series({
    'Start date': start_date,
    'End date': end_date,
    'Time period (days)': time_delta.days,
    'Assets': len(symbols),
    'Window length': window_len,
    'Windows': window_count,
    'Exit types': len(exit_types),
    'Stop values': len(stops),
    'Tests per asset': window_count * len(stops) * len(exit_types),
    'Tests per window': len(symbols) * len(stops) * len(exit_types),
    'Tests per exit type': len(symbols) * window_count * len(stops),
    'Tests per stop type and value': len(symbols) * window_count,
    'Tests total': len(symbols) * window_count * len(stops) * len(exit_types)
}))
