#!/bin/bash

# Check for virtual environment
if [ -d "venv" ]; then
    echo "Virtual environment found."
else
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run setup_core.py
python setup_core.py

# Launch Streamlit
streamlit run app.py