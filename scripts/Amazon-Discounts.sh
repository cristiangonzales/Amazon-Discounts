#!/bin/sh

cd ..
docker build -t amazon-discounts .
docker run amazon-discounts
