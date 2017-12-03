@ECHO OFF
REM Amazon Discount Finder. All rights reserved.
REM Author: Cristian Gonzales

REM This script assumes you have Python3.6 and pip3 installed on your machine
REM pip install all required dependences
pip3 install bs4 && pip3 install gevent && pip3 install selenium && pip3 install python-amazon-simple-product-api && pip3 install pypiwin32

REM Go into the src folder and run the program
CD ..\amazondiscounts.src\main
python3 AMZNMain.py
