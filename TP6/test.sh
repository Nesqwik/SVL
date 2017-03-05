#!/bin/bash

rm -rf data_current.json
cp -R data_test.json data_current.json
python3 server.py data_current.json
