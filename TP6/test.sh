#!/bin/bash

rm -rf data_current
cp -R data_test data_current
python3 server.py data_current
