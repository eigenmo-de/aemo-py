#!/bin/sh

# check coverage
coverage report -m aemo/__init__.py aemo/key.py  aemo/tables/__init__.py aemo/tables/settlements.py

# run unit tests

pytest -v
