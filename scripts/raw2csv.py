from pathlib import Path
import json
from datetime import datetime

MINTING_ACCOUNT = None
MINTER_ACCOUNT_ALIAS = 'revenue:icp:minter'

# Load inbound account identifiers.
inbound_accounts = dict([tuple(reversed(a.strip().split(','))) for a in open('accounts/inbound_accounts.txt').readlines()[1:]])

own_accounts = {}
first = True
for own_account in open('accounts/own_accounts.txt').readlines():
    if first:
        # skip first line.
        first = False
        continue
    own_account = own_account.strip().split(',')
    # Mapping account identifier to (alias, neuron_id)
    own_accounts[own_account[2]] = (own_account[0], own_account[1])

# iterate over account identifier files.
txs = set()
account_files = Path('raw').glob('*')
for account_file in account_files:
    for data in open(account_file):
        # Remove new lines.
        data = data.strip()
        data = json.loads(data)

        for block in data['blocks']:
            sender = block['from_account_identifier']
            receiver = block['to_account_identifier']
            sender_alias = ''
            fee = int(block['fee'])
            if sender in inbound_accounts:
                amount_sent = int(block['amount'])
                sender_alias = "revenue:icp:%s" % inbound_accounts[sender]
                # Don't account the fee they pay in my records.
                fee = 0
            else:
                # sender is not dfinity, then it _must_ be one of my accounts
                # or the minting account.
                assert sender in own_accounts or sender == MINTING_ACCOUNT, "Account ID %s not found. It's either an account you own (which you should add to accounts.txt), or an inbound account (add to inbound_accounts.txt)" % sender

                # Since we're the sender, include the fees in the money
                # we're sending.
                amount_sent = int(block['amount']) + int(block['fee'])

                if sender:
                    sender_alias = 'assets:icp:%s:%s' % (own_accounts[sender][0], sender)
                else:
                    sender_alias = MINTER_ACCOUNT_ALIAS


            receiver_alias = 'expenses:icp:%s' % receiver
            if receiver in own_accounts:
                receiver_alias = 'assets:icp:%s:%s' % (own_accounts[receiver][0], receiver)

            amount_received = int(block['amount'])

            txs.add((
                block['block_height'],
                block['parent_hash'],
                block['block_hash'],
                block['transaction_hash'],
                sender,
                sender_alias,
                receiver,
                receiver_alias,
                block['transfer_type'],
                amount_sent / 100000000.0,
                amount_received / 100000000.0,
                fee / 100000000.0,
                block['memo'],
                str(datetime.fromtimestamp(block['created_at']))
            ))

for tx in txs:
    print(*tx, sep=',')
