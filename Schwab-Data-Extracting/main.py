import sys
from datetime import timedelta

import pandas as pd
import schwabdev

TICKERLIST = sys.argv[1]
DAYS = int(sys.argv[2])
COLUMNS = ['DateTime', 'Open', 'High', 'Low', 'Close', 'Volume']

def get_days_data(ticker, days):
	try:
		data = client.price_history(self, ticker, periodType='day', period=days)
	except:
		print(f'Symbol {ticker} is not found.')
		data = {}
	return data

def get_mins_data(ticker, days):
	mins = timedelta(days=-days)
	try:
		data = client.price_history(self, ticker, periodType='min', period=mins)
	except:
		print(f'Symbol {ticker} is not found.')
		data = {}
	return data

# connect to Schwab
client = schwabdev.Client('Your app key', 'Your app secret')
client.update_tokens_auto()

# collect data for each ticker
with open(TICKERLIST, 'r') as f:
	for ticker in f:
		ticker.strip()

		data_days = get_days_data(ticker, DAYS) 
		data_days = pd.read_json(data_days)
		data.to_csv(f'/data/1D/{ticker}_1D.csv', columns = COLUMNS)

		data_mins = get_mins_data(ticker, DAYS)
		data_mins = pd.read_json(data_mins)
		data.save_to_csv(f'/data/1M/{ticker}_1M.csv', columns = COLUMNS)
