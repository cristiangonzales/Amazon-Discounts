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
docker pull selenium/standalone-chrome:3.7.1-cadmium > /dev/null 2>&1

# Run the image detached
docker run --privileged -d -p 4444:4444 selenium/standalone-chrome:3.7.1-cadmium > /dev/null 2>&1

# Go back one level to build our container
cd ..

# Build and run our Docker container, giving it the same network attributes as our local machine
docker build -q -t amazon-discounts . > /dev/null 2>&1
docker run --interactive --tty --net=host amazon-discounts

# After execution, we want to copy our log file into the root directory of this repo
echo Obtaining log file...
id=$(docker ps -a | grep amazon-discounts | awk '{ print $1 }')
docker cp $id:/usr/amazon-discounts.log .
docker cp $id:/usr/failed-proxies.log .

# Stop and remove all containers once these processes are over
docker kill $(docker ps -q) > /dev/null 2>&1
docker rm $(docker ps -a -q) > /dev/null 2>&1
