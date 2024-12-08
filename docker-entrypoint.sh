#!/bin/bash

# Activate Conda environment
source /venv/bin/activate

# Run the Python script with all passed arguments
python app.py "$@"