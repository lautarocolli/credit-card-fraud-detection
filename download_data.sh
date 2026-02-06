#!/usr/bin/env bash
set -e

DATA_DIR="data"
DATASET="mlg-ulb/creditcardfraud"

echo "Creating data directory..."
mkdir -p "$DATA_DIR"

if ! command -v kaggle &> /dev/null; then
  echo "ERROR: Kaggle CLI not found."
  echo "Please install it and authenticate first:"
  echo "https://www.kaggle.com/docs/api"
  exit 1
fi

echo "Downloading dataset from Kaggle..."
kaggle datasets download -d "$DATASET" -p "$DATA_DIR"

echo "Extracting dataset..."
unzip -o "$DATA_DIR/creditcardfraud.zip" -d "$DATA_DIR"

echo "Cleaning up zip file..."
rm "$DATA_DIR/creditcardfraud.zip"

echo "Dataset downloaded successfully."
