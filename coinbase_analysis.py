import coinbase as cb
from coinbase.wallet.client import Client
import json

CURRENCY_TYPE = ["BTC", "ETH", "LTC"]

def json_account_to_dict(client):
    all_accounts_dict = json.loads(json.dumps(client.get_accounts()))
    cleaned_accounts_dict = json.loads(json.dumps(all_accounts_dict['data']))
    return cleaned_accounts_dict

#Grab the account ID for: ALL(dict), BTC, ETH or LTC(id string)
def get_account_id(client, currency = "ALL"):
    if currency not in CURRENCY_TYPE and currency != "ALL":
        raise TypeError('Wrong currency type: %s' % currency)
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
        if currency in CURRENCY_TYPE:
            res = res[currency+str(' in USD')]
    else:
        for a in range(num_of_accounts):
            res.update({accounts_dict[a].get('balance').get('currency')
                       : accounts_dict[a].get('balance').get('amount')})
        if currency in CURRENCY_TYPE:
            res = res[currency]
    return res

#Grab the current total account balance in USD
def get_total_account_balance_USD(client):
    return sum([float(i) for i in get_account_balance(client).values()])


# Working on:
## grab all "completed" transaction history in a currency wallet
## interested type includes: buy, sell, send
## documentation on Transaction class: https://developers.coinbase.com/api/v2#transaction-resource
## assuming native currency is USD only for now
## note: transaction on the way but not instantly available in wallet are not counted in the method
def calc_roi_alltime(client, currency):
    all_transactions = json.loads(json.dumps(client.get_transactions(get_account_id(client,currency))))
    cleaned_all_transactions = json.loads(json.dumps(all_transactions['data']))
    completed_transactions = [cleaned_all_transactions[a] for a in range(len(cleaned_all_transactions)) if cleaned_all_transactions[a].get('status') == 'completed']
    all_type_list = [completed_transactions[a].get('type') for a in range(len(completed_transactions))]
    buy_id_list = [i for i, x in enumerate(all_type_list) if x == "buy"]
    sell_id_list = [i for i, x in enumerate(all_type_list) if x == "sell"]
    send_id_list = [i for i, x in enumerate(all_type_list) if x == "send"]
    # record USD value sum of all buy
    all_buy_value = sum([float(completed_transactions[a].get('native_amount').get('amount')) for a in buy_id_list])
    # record USD value sum of all sell
    all_sell_value = sum([float(completed_transactions[a].get('native_amount').get('amount')) for a in sell_id_list])
    all_send_value = sum([float(completed_transactions[a].get('native_amount').get('amount')) for a in send_id_list])
    # grab the current USD value in the currency wallet
    current_balance = float(get_account_balance(client, currency))
    r = - all_sell_value - all_send_value + current_balance - all_buy_value
    roi = r*1.0/all_buy_value
    return roi





