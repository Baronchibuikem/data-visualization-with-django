#!/usr/bin/env bash

# run mypy
echo "-------------------------------------------------------"
echo "Running mypy..."
echo "-------------------------------------------------------"
cd src
mypy .
cd ..