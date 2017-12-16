# Coinbase API test

## Setup
1. `pip install -r requirements.txt`
2. Fill in your [API key and secret](https://support.coinbase.com/customer/portal/articles/1914910-how-can-i-generate-api-keys-for-my-merchant-account-) in a local file called `api_key`.

* Note: Please make sure that your API allows all read access; as of now, the code doesn't make any actions such as buy & sell, so no need of granting further access other than read type 

e.g. `api_key` textfile should look like:
```
YOUR_API_KEY
YOUR_API_SECRET
```
3. run `python test_api.py`
