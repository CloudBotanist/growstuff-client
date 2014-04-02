#!/bin/sh

if [ $(whoami) != "pi" ]; then
	echo "You need pi user privileges to run this script"
    exit 0
fi

# Installing virtualenv
sudo easy_install-pypy virtualenv

# Creating the virtual python environnement
/usr/lib/pypy-upstream/bin/virtualenv ~/.socketenv

# Activating the environnement to install socketIO and pySerial
sudo su pi -c "source ~/.socketenv/bin/activate"

# Installing the dependecies
~/.socketenv/bin/pip install -U pySerial socketIO-client dropbox

# Installing Pico (only pico client has been forked)
wget https://raw.githubusercontent.com/alexisfasquel/growstuff-connector-server/master/init/init.sh -O - | sudo sh

# Dowloading the repo and unziping
rm -R /tmp/growstuff-client-master 2>/dev/null
rm master.zip 2>/dev/null
wget https://github.com/alexisfasquel/growstuff-client/archive/master.zip
unzip -d /tmp master.zip

# Moving and renaming the "firmware"
mv /tmp/growstuff-client-master/rasp-firmware ~/growstuff

# Adding the startup command
replacement="cd /home/pi/growstuff ; sudo ./growstuff.sh > growstuff.log 2>&1 &" 
sudo sed -i "/exit 0$/i \\$replacement\n" /etc/rc.local
