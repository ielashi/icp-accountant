# ICP Scraper

## Requirements

Python3 `python3`
Hledger `hledger` (`brew install hledger`)

Install python requirements.

```
pip3 install requests
```

## Setup your accounts

1. Lookup the account identifiers of all your liquid ICP accounts and neurons, and add them to `accounts/own_accounts.txt`. Each account should have an alias for easier reporting.

```
alias,neuron-id,account_identifier
main_icp_account,,1111111112222222222222333333333333333334444444444555555555556666
another_icp_account,,7777777777778888888888999999999999999999aaaaaaaaaaabbbbbbbbbbbbb
my_neuron,123123,1111111112222222222222333333333333333334444444444555555555556666
my_other_neuron,365653,7777777777778888888888999999999999999999aaaaaaaaaaabbbbbbbbbbbbb
```

NOTE: Make sure you add _all_ your neurons, including ones you've dissolved and have a balance of zero, as these will also be needed for accounting purposes.

2. `inbound_accounts.txt` is a list of account identifiers that you've received ICP from (e.g. DFINITY). You don't necessarily need to fill this initially. The scripts will throw errors that will help you fill it out.

```
alias,account_identifier
dfinity,1111111112222222222222333333333333333334444444444555555555556666
```

## Download ICP transactions

Once you've filled your `own_accounts.txt`, you can download you transactions by running:

```
make fetch
```

This will store all the raw transaction data in the `raw` folder. I recommend committing that into the repo to track how they evolve over time.

## Generate reports

To generate the reports run:

```
make report
```

Reports will be stored in the `reports` folder. I recommend also committing these in the repor.
