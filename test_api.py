import coinbase_analysis as cba
from coinbase.wallet.client import Client

# read API key and secret from file
api_file = open('api_key.txt', 'r')
API_KEY = api_file.readline()[:-1]  # your API key
API_SECRET = api_file.readline()[:-1]  # your API secret
print 'API key:', API_KEY

client = Client(API_KEY, API_SECRET)


def print_all_balance(client):
    balances = cba.get_account_balance(client, ifUSD=False)
    for k, v in balances.items():
        print '%s: %.4f' % (k, float(v))


# Print balance for all currencies
print '=== Account Balance ==='
print_all_balance(client)
print

# Calculate alltime ROI for each wallet
print '=== ROI ==='
print 'BTC: %f' % cba.calc_roi_all_time(client, 'BTC')
print 'ETH: %f' % cba.calc_roi_all_time(client, 'ETH')
print 'LTC: %f' % cba.calc_roi_all_time(client, 'LTC')
print

# Net income
print '=== Net Income ==='
print 'BTC: %f' % cba.calc_net_income(client, 'BTC')
print 'ETH: %f' % cba.calc_net_income(client, 'ETH')
print 'LTC: %f' % cba.calc_net_income(client, 'LTC')
