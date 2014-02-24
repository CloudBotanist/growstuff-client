growstuff-client
================
**The pi:** The following configuration has been done with raspbian Wheezy on the pi. 

###Dependances

- virtualenv
- socketIO-client
- pySerial

####Step by step
Installing virutalenv,

    sudo easy_install-pypy virtualenv

And then creating the virtual python environnement:
    
    virtualenv  ~/.socketenv
    
Unfortunatly, the binaries may not have been added to the path, you will need to lanch it from the source:

    /usr/lib/pypy-upstream/bin/virtualenv ~/socketenv
    
Activating the environnement to install socketIO and pySerial

    source ~/.socketenv/bin/activate
    
Then install the dependecies:

    pip install -U pySerial socketIO-client
    
You may also have an issue with pip, then once again:

    sudo ./sockentenv/bin/pip install -U pySerial socketIO-client


and leave the environnement:

    deactivate

###INSTALLATION :

VIRTUAL_ENV=$HOME/.virtualenv

####Prepare isolated environment
virtualenv $VIRTUAL_ENV

####Activate isolated environment
source $VIRTUAL_ENV/bin/activate

####Install package
pip install -U socketIO-client


####More info : 
https://pypi.python.org/pypi/socketIO-client


####ROADMAP : 

- HAndle sockeIO excpetion
- Reconnect loop after disconnection ?
- Improve the integration (redirection to log, varialble path...)
