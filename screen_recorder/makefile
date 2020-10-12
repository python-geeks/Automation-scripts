VENV ?= .venv
REQUIREMENTS_FILE ?= requirements.txt

init:
	python3 -m venv $(VENV)
	$(VENV)/bin/python -m pip install --upgrade pip
	if [ -f $(REQUIREMENTS_FILE) ]; \
	    then $(VENV)/bin/python -m pip install -r $(REQUIREMENTS_FILE); \
    fi