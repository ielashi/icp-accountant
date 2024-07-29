# Define for reporting period (optional)
FROM_DATE ?= "2021-05-01"
TO_DATE ?= $(shell date +%Y-%m-%d)


fetch:
	python3 scripts/fetch_transactions.py

report:
	bash scripts/generate_reports.sh $(FROM_DATE) $(TO_DATE)
