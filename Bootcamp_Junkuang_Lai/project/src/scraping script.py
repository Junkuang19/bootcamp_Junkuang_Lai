import pandas as pd
import requests
import numpy as np


# Download stock data from yfinance
SYMBOL = 'NVDA'
import yfinance as yf
df_api = yf.download(SYMBOL, period='6mo', interval='1d', auto_adjust=True).reset_index()
# Use 'Adj Close' if present, else use 'Close'
if 'Adj Close' in df_api.columns:
    df_api = df_api[['Date', 'Adj Close']]
    df_api.columns = ['date', 'adj_close']
elif 'Close' in df_api.columns:
    df_api = df_api[['Date', 'Close']]
    df_api.columns = ['date', 'adj_close']
else:
    raise ValueError("No 'Adj Close' or 'Close' column found in yfinance data")
