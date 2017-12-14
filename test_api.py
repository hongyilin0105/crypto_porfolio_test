import coinbase as cb
from coinbase.wallet.client import Client
import json

API_KEY = '' # your API key
API_SECRET = '' # your API secret
client = Client(API_KEY, API_SECRET)

user = client.get_current_user()
user_as_json_string = json.dumps(user)

def json_account_to_dict(client):
    all_accounts_dict = json.loads(json.dumps(client.get_accounts()))
    cleaned_accounts_json_string = json.dumps(all_accounts_dict['data'])
    cleaned_accounts_dict = json.loads(cleaned_accounts_json_string)
    return cleaned_accounts_dict

#Grab the account ID for: ALL(dict), BTC, ETH or LTC(id string)
def get_account_id(client, currency = "ALL"):
    if currency not in ["ALL", "BTC", "ETH", "LTC"]:
        return "you suck"
    wallet_name = currency + str(" Wallet")
    accounts_dict = json_account_to_dict(client)
    num_of_accounts = len(accounts_dict)
    res = {}
    for a in range(num_of_accounts):
        res.update({accounts_dict[a].get('name')
                    : accounts_dict[a].get('id')})
    if currency == "ALL":
        return res
    else:
        return res[wallet_name]

#For US-native accounts, grab the current account balance for: BTC, ETH or LTC(float)
#Default: USD value for all currencies
def get_account_balance(client, currency = "ALL", ifUSD = True):
    accounts_dict = json_account_to_dict(client)
    num_of_accounts = len(accounts_dict)
    res = {}
    if ifUSD:
        for a in range(num_of_accounts):
            res.update({accounts_dict[a].get('balance').get('currency')+str(' in USD')
                        : accounts_dict[a].get('native_balance').get('amount')})
        if currency in ["BTC", "ETH", "LTC"]:
            res = res[currency+str(' in USD')]
    else:
        for a in range(num_of_accounts):
            res.update({accounts_dict[a].get('balance').get('currency')
                       : accounts_dict[a].get('balance').get('amount')})
        if currency in ["BTC", "ETH", "LTC"]:
            res = res[currency]
    return res


get_account_balance(client, False)
