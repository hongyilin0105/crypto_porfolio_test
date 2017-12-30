#import binance
from binance.client import Client
import string

api_file = open('binance_api_key.txt', 'r')
API_KEY = api_file.readline()[:-1]  # your API key
API_SECRET = api_file.readline()[:-1]  # your API secret
client = Client(API_KEY, API_SECRET)

#print all trade history for trading pairs of interest
with open('interested_pairs.txt', 'r') as pairs:
    for pair in pairs:
        symbol = string.replace(pair, '\n','')
        print symbol +":"
        print client.get_historical_trades(symbol=symbol)