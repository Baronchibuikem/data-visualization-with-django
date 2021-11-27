#!/usr/bin/env bash

# run black - make sure everyone uses the same python style
echo "-------------------------------------------------------"
echo "checking files in src folder..."
echo "-------------------------------------------------------"
black src
echo "-------------------------------------------------------"
echo "checking files in tests folder.."
echo "-------------------------------------------------------"
black tests