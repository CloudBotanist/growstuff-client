#!/bin/bash

cd "`dirname $0`"

if [ "$1" == "" ]; then
	if [ ! -f ./plant.conf ]; then
		echo "No ID found (missing plant.conf)"
		exit 0
	fi
else
	echo $1 > plant.conf
fi

VIRTUAL_ENV=~pi/.socketenv
sudo su pi -c "source $VIRTUAL_ENV/bin/activate"

sudo pypy client.py

exit 0
