#!/usr/bin/env bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
echo ""
echo "Virtual environment created and requirements installed."
echo "Run with: source .venv/bin/activate && streamlit run app.py"
