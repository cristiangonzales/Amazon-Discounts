#!/bin/sh
# Amazon Discount Finder. All rights reserved.
# Author: Cristian Gonzales

# Check if virtualenv is installed. If so, continue, and if not, then go ahead and install it.
if python -c "import virtualenv" &> /dev/null; then
    continue
else
    pip install virtualenv
fi

# Check to see if a virtualenv variable is configured. If it isn't, then we will go one level above
# the repository, create a virtual environment, move the Amazon-Discounts repository into the ENV/
# directory, go into the ENV/ directory, activate the virtualenv, and then go back into the
# Amazon-Discounts/scripts directory. Then, we will pip install all of the dependencies
if [[ -z "${VIRTUAL_ENV}" ]]; then
	cd ../../
	virtualenv ENV
	mv Amazon-Discounts ENV/
	cd ENV/
	source bin/activate
	cd Amazon-Discounts/scripts

	# TODO: pip install all required dependencies here

# This else conditional assumes that you have ran the script once and already have all the required
# packages and dependencies installed.
else
	continue

# Go into the src folder and run the program
cd ../amazondiscounts.src/main/
python AMZNMain.py
