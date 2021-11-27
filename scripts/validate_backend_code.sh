#!/usr/bin/env bash

# run black - make sure everyone uses the same python style
echo "-------------------------------------------------------"
echo "Running black..."
echo "-------------------------------------------------------"
echo "-------------------------------------------------------"
echo "checking files in src folder..."
echo "-------------------------------------------------------"
black .
echo "-------------------------------------------------------"
echo "checking files in tests folder..."
echo "-------------------------------------------------------"
#black tests

echo "-------------------------------------------------------"
echo "fixing imports arrangement with isort.."
echo "-------------------------------------------------------"
isort .

# run mypy
echo "-------------------------------------------------------"
echo "Running mypy..."
echo "-------------------------------------------------------"
mypy .

# run python static validation
echo "-------------------------------------------------------"
echo "Running prospector..."
echo "-------------------------------------------------------"
prospector  --profile-path=. --profile=.prospector.yaml --path=. --ignore-patterns=static

# run bandit - A security linter from OpenStack Security
echo "-------------------------------------------------------"
echo "Running bandit..."
echo "-------------------------------------------------------"
bandit -r .

echo "-------------------------------------------------------"
echo "Running pytest..."
echo "-------------------------------------------------------"
#py.test --disable-socket --nomigrations -W error::RuntimeWarning --reuse-db --cov=src --cov-report html:test_cov_report tests/

echo "-------------------------------------------------------"
echo "END OF SCRIPT"
echo "-------------------------------------------------------"