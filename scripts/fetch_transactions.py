from datetime import datetime
import requests
import os

TRANSACTIONS_API_URL = 'https://ledger-api.internetcomputer.org/accounts/%s/transactions?limit=100'

# Read the list of accounts to lookup, skipping the headers line.
for account in open('accounts/own_accounts.txt').readlines()[1:]:
    account_identifier = account.strip().split(',')[2]

    # Fetch the transactions from the dashbaord api.
    url = TRANSACTIONS_API_URL % account_identifier
    response = requests.get(url)

    # The raw folder is where we store the raw (unprocessed) transactions as retrieved from
    # the API.
    if not os.path.exists('raw'):
        os.makedirs('raw')

    file = open('raw/%s.json' % account_identifier, 'w')
    file.write(response.text)
    file.close()
