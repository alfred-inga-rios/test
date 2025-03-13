test: test-unit

test-unit:
	poetry run pytest -m "not (integration or slow)" --cov=. --cov-report=xml:coverage.xml --cov-branch