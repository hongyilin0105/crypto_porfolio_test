import coinbase_analysis as cba
from coinbase.wallet.client import Client
import json

# read API key and secret from file
api_file = open('api_key.txt', 'r')
API_KEY = api_file.readline()[:-1] # your API key
API_SECRET = api_file.readline() # your API secret
print 'API key:', API_KEY

client = Client(API_KEY, API_SECRET)

#user = client.get_current_user()
#user_as_json_string = json.dumps(user)

#Example
print cba.get_account_balance(client, ifUSD = False)
print cba.get_account_balance(client, "ETH", False)
print cba.get_total_account_balance_USD(client)

#Calculate alltime ROI for each wallet
print "BTC roi: " + str(cba.calc_roi_alltime(client, "BTC"))
print "ETH roi: " + str(cba.calc_roi_alltime(client, "ETH"))
print "LTC roi: " + str(cba.calc_roi_alltime(client, "LTC"))
