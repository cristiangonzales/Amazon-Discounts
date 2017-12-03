#!/bin/sh
# Amazon Discount Finder. All rights reserved.
# Author: Cristian Gonzales

# NOTE: This script assumes you have Python3.6 and pip3 installed on your machine.
# pip install all required dependencies
pip3 install bs4 && pip3 install gevent && pip3 install selenium && pip3 install python-amazon-simple-product-api

# Go into the src folder and run the program
cd ../amazondiscounts.src/main/
python3 AMZNMain.py
