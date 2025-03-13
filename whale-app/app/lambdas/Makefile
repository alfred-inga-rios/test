test: test-unit test-integration

test-unit:
	poetry run pytest -m "not (integration or slow)" --cov=. --cov-report=xml:coverage_unit_tests.xml --cov-branch

test-integration:
	poetry run pytest -m integration --cov=. --cov-report=xml:coverage_integration_tests.xml --cov-branch