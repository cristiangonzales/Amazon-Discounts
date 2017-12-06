#!/bin/sh
# Amazon Discount Finder. All rights reserved.
# Author: Cristian Gonzales

# NOTE: This script assumes you have Python3.6 and pip3 installed on your machine.
# pip install all required dependencies
pip3 install bs4 > /dev/null 2>&1 && pip3 install gevent > /dev/null 2>&1 && pip3 install selenium > /dev/null 2>&1 && pip3 install python-amazon-simple-product-api > /dev/null 2>&1

# Go into the src folder and run the program
cd ../amazondiscounts.src/main/
python3 AMZNMain.py
