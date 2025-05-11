#!/bin/bash

# --- Installation of requirements ---
echo "Installing requirements from requirements.txt..."
if pip install -r requirements.txt; then
  echo "Requirements installed successfully."
else
  echo "Error installing requirements. Please check requirements.txt."
  exit 1
fi

echo ""

# --- Execution of setup scripts ---
echo "Executing setup scripts..."

echo "Running seed_data.py..."
if python seed_data.py; then
  echo "seed_data.py executed successfully."
else
  echo "Error executing seed_data.py."
  exit 1
fi

echo ""

 echo "Running download_nltk_resources.py..."
 if python download_nltk_resources.py; then
   echo "download_nltk_resources.py executed successfully."
 else
   echo "Error executing download_nltk_resources.py."
   exit 1
 fi

echo ""

echo "Setup complete!"
exit 0