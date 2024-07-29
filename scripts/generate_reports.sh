set -euo pipefail

JOURNAL=icp.journal
FROM_DATE="$1"
TO_DATE="$2"

# remove the journal to trigger a full reimport
mkdir -p journal
rm -rf journal/$JOURNAL journal/.latest.*

# Parse transactions
python3 scripts/raw2csv.py > journal/transactions.csv

# Import them into hledger
hledger -f journal/$JOURNAL import journal/transactions.csv --rules-file icp.rules

# Generate reports
mkdir -p reports
hledger -f journal/$JOURNAL incomestatement  --begin=$FROM_DATE --end=$TO_DATE > reports/income_statement_${FROM_DATE}_${TO_DATE}.txt
hledger -f journal/$JOURNAL balancesheet  --begin=$FROM_DATE --end=$TO_DATE > reports/balance_sheet_${FROM_DATE}_${TO_DATE}.txt
