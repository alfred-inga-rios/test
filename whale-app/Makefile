test: test-unit

test-unit:
	poetry run pytest -m "not (integration or slow)" --cov=src --cov-report=xml:.coverage-reports/coverage_unit_tests.xml --cov-branch