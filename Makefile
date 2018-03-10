test_cmd = pytest
coverage_cmd = coverage combine && coverage report
lint_cmd = prospector

install:
	$(info * Installing Python package...)
	python3 setup.py install

install-test-dependencies:
	$(info * Installing Python test dependencies...)
	pip3 install -e .\[test\]

lint:
	$(info * Running linter...)
	$(lint_cmd)

test:
	$(info * Running tests w/ coverage measurement...)
	# unfortunately pytest-cov doesn't measure subprocesses with
	# multiprocessing_scheduler, pytest-cov v2.4.0, coverage v4.2:
	#$(PYTEST) --cov=. --cov-report=term
	# using this workaround instead,
	# which goes through a sitecustomize.py file inside $(PWD)/enable_coverage/:
	export PYTHONPATH=$(PWD)/enable_coverage:$(PYTHONPATH) && $(test_cmd)
	$(coverage_cmd)

testnocov:
	$(info * Running tests w/o coverage measurement...)
	$(test_cmd)

.PHONY: install install-test-dependencies lint test testnocov