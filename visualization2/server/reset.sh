#!/bin/bash

rm -rf augmentedDataset/validation/*
rm -rf augmentedDataset/train/*
rm -rf dataset/*

FILE=dataset.zip

if test -f "$FILE"; then
	rm "$FILE"
fi

python3 resetJson.py
