import coinbase_analysis as cba
from coinbase.wallet.client import Client
import json

API_KEY = 'tjSOJDfiJ5pX2xoD' # your API key
API_SECRET = 'hSaGcd5jvGrbi9O5RwCFIyxz2qt3EjLT' # your API secret
client = Client(API_KEY, API_SECRET)

#user = client.get_current_user()
#user_as_json_string = json.dumps(user)

#Example
print cba.get_account_balance(client, ifUSD = False)
print cba.get_account_balance(client, "ETH", False)
print cba.get_total_account_balance_USD(client)