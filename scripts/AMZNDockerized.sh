#!/bin/sh
# Amazon Discount Finder. All rights reserved.
# Author: Cristian Gonzales

cd ..
docker build -t amazon-discounts .
docker run amazon-discounts
