VENV := venv
PYTHON := $(VENV)/bin/python

RM := rm -rf

.PHONY: venv clean-build clean-api clean api build docs clean-docs

venv:
	$(RM) $(VENV)
	python3 -m venv $(VENV)
	$(PYTHON) -m pip install -U pip wheel setuptools
	$(PYTHON) -m pip install -U -r requirements.txt -r dev-requirements.txt
	@echo "Created venv with $$($(PYTHON) --version)"

clean-docs:
	$(RM) docs/source/build

docs:
	make clean-docs
	cd docs/compiler && ../../$(PYTHON) compiler.py
	$(VENV)/bin/sphinx-build \
		-b html "docs/source" "docs/source/build/html" -j6