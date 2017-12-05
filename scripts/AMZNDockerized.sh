#!/bin/sh
# Amazon Discount Finder. All rights reserved.
# Author: Cristian Gonzales

# Conditional to see if Docker is running. If not, we will open it for the client.
if ps aux | grep Docker | grep -v grep > /dev/null
then
	open -a Docker
else
	continue
fi

# Pull standalone Chrome (debug because we don't know the behavior of our program)
docker pull selenium/standalone-chrome:3.7.1-cadmium

# Run the image detached
docker run --privileged -d -p 4444:4444 selenium/standalone-chrome:3.7.1-cadmium

# Go back one level to build our container
cd ..

# Build and run our Docker container, giving it the same network attributes as our local machine
docker build -t amazon-discounts .
docker run --net=host amazon-discounts

# Stop and remove all containers once these processes are over
docker kill $(docker ps -q)
docker rm $(docker ps -a -q)
