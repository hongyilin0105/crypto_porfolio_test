#import binance
from binance.client import Client

api_file = open('binance_api_key.txt', 'r')
API_KEY = api_file.readline()[:-1]  # your API key
API_SECRET = api_file.readline()[:-1]  # your API secret
client = Client(API_KEY, API_SECRET)

interested_pairs = open('interested_pairs.txt', 'r')

while interested_pairs:
    pair = interested_pairs.readline()[:-1]
    print str(pair)+":"
    print client.get_historical_trades(symbol=pair)