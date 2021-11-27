#!/usr/bin/env bash

# run python static validation
echo "-------------------------------------------------------"
echo "Running prospector..."
echo "-------------------------------------------------------"
prospector  --profile-path=. --profile=.prospector.yaml --path=src --ignore-patterns=static
