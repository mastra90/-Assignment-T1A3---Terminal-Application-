#!/usr/bin/env bash

for file in *.py; do
	echo "Running $file..."
	python3 "$file"
done