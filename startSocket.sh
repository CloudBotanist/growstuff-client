VIRTUAL_ENV=/home/pi/.socketenv
sudo su pi -c "source $VIRTUAL_ENV/bin/activate"

pypy /home/pi/socket/client.py &
