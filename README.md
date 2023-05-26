# ICP Accountant

Your personal accountant for all things ICP.

This tool can generate:

1. **A balance sheet**, containing all your ICP assets, for any duration. Example:

```
                                                                                          ||        2023-05-21
==========================================================================================++===================
 Assets                                                                                   ||
------------------------------------------------------------------------------------------++-------------------
 assets:icp:my_icp_account:my_icp_address                                                 ||   ICP100.00000000
 assets:icp:my_neuron:my_neuron_address.                                                  ||   ICP100.00000000
------------------------------------------------------------------------------------------++-------------------
                                                                                          ||   ICP200.00000000
==========================================================================================++===================
 Liabilities                                                                              ||
------------------------------------------------------------------------------------------++-------------------
------------------------------------------------------------------------------------------++-------------------
                                                                                          ||
==========================================================================================++===================
 Net:                                                                                     ||   ICP200.00000000
```

2. **Income statement**, containing how much ICP you've received, minted, and paid, for any duration. Example:
```
                                                                               || 2021-05-01..2023-05-21
===============================================================================++========================
 Revenues                                                                      ||
-------------------------------------------------------------------------------++------------------------
 revenue:icp:dfinity                                                           ||        ICP100.00004000
 revenue:icp:minter                                                            ||         ICP10.00000000
-------------------------------------------------------------------------------++------------------------
                                                                               ||        ICP110.00000000
===============================================================================++========================
 Expenses                                                                      ||
-------------------------------------------------------------------------------++------------------------
 expenses:icp:some_payment_account                                             ||         ICP10.00000000
 expenses:icp:fee                                                              ||          ICP0.00004000
-------------------------------------------------------------------------------++------------------------
                                                                               ||         ICP10.00004000
===============================================================================++========================
 Net:                                                                          ||        ICP100.00004000
```

## Requirements

You'll need to have the following on your path:

* `python3`
* `hledger` (`brew install hledger`)
* Install the `requests` python package: `pip3 install requests`

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
