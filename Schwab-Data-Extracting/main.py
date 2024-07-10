import sys
from datetime import deltatime

import pandas as pd
import schwabdev


TICKERLIST = sys.argv[1]
DAYS = int(sys.argv[2])
COLUMNS = ['DateTime', 'Open', 'High', 'Low', 'Close', 'Volume']


def get_days_data(ticker, days):
	data = request_api_data
	data =
	return data

def get_mins_data(ticker, days):
	mins = timedelta(
		days=-days,
		hours=-now.hour,
		minutes=-now.minute,
		seconds=-now.second
	)
	data = request_api_data
	data = 
	return data



client = schwabdev.Client('Your app key', 'Your app secret')
client.update_tokens_auto()


with open(TICKERLIST, 'r') as f:
	for ticker in f:
		ticker.strip()
		
		data_days = get_days_data(ticker, DAYS) 
		data_days = pd.read_json(data_days)
		data.to_csv(f'/data/1D/{ticker}.csv', columns = COLUMNS)

		data_mins = get_mins_data(ticker, DAYS)
		data_mins = pd.read_json(data_mins)
		data.save_to_csv(f'/data/1M/{ticker}.csv', columns = COLUMNS)
