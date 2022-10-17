#!/bin/bash -xe

pycodestyle .
python ./run-pyflakes.py
python ./run-mccabe.py 10
pylint ./test.py