if [ "$0" == "" ]; then
	if [ ! -f plant.conf ]; then 
		echo "No ID found (missing plant.conf)"
		exit 0
	fi
fi

VIRTUAL_ENV=/home/pi/.socketenv
sudo su pi -c "source $VIRTUAL_ENV/bin/activate"

pypy /home/pi/socket/client.py &
