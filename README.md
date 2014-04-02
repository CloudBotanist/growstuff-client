growstuff-client
================
**The pi:** The following configuration has been done with raspbian Wheezy on the pi. 

###Dependances

- virtualenv
- socketIO-client
- pySerial
- dropbox

####Step by step
Installing virutalenv,

    sudo easy_install-pypy virtualenv

And then creating the virtual python environnement:
    
    virtualenv  ~/.socketenv
    
Unfortunatly, the binaries may not have been added to the path, you will need to lanch it from the source:

    /usr/lib/pypy-upstream/bin/virtualenv ~/.socketenv
    
Activating the environnement to install socketIO and pySerial

    source ~/.socketenv/bin/activate
    
Then install the dependecies:

    pip install -U pySerial socketIO-client dropbox
    
You may also have an issue with pip, then once again:

    sudo ./.sockentenv/bin/pip install -U pySerial socketIO-client dropbox


and leave the environnement:

    deactivate

##### Running the script at startup :

     sudo nano /etc/rc.local

 Adding the following snippet juste before the **exit 0** (considering that the variable **path** does not already exists)

     cd /home/pi/growstuff ; sudo ./socket.sh > socket.log 2>&1 &
