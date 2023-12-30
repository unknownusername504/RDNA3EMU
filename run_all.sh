#!/bin/bash

# Create a virtual environment
python -m venv env

# Activate the virtual environment
source env/bin/activate

# Install the package
python setup.py install

# Run all the tests in Data\test_list.txt
python -m unittest test_all.py

# Deactivate the virtual environment
deactivate