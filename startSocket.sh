if [ "$1" == "" ]; then
	if [ ! -f plant.conf ]; then 
		echo "No ID found (missing plant.conf)"
		exit 0
	fi
else
	echo $1 > plant.conf
fi

VIRTUAL_ENV=/home/pi/.socketenv
sudo su pi -c "source $VIRTUAL_ENV/bin/activate"

sudo pypy /home/pi/socket/client.py > socket.log 2>&1&
