set -euo pipefail

JOURNAL=icp.journal

# remove the journal to trigger a full reimport
mkdir -p journal
rm -rf journal/$JOURNAL journal/.latest.*

# Parse transactions
python3 scripts/raw2csv.py > journal/transactions.csv

# Import them into hledger
hledger -f journal/$JOURNAL import journal/transactions.csv --rules-file icp.rules

# Generate reports
mkdir -p reports
hledger -f journal/$JOURNAL incomestatement > reports/income_statement.txt
hledger -f journal/$JOURNAL balancesheet > reports/balance_sheet.txt
