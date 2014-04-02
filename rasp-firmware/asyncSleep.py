import threading
import time

class AsyncSleep(threading.Thread):
    def __init__(self, sleepTime, callBack):
        threading.Thread.__init__(self)
        self.sleepTime = sleepTime
        self.callBack = callBack;

    def run(self):
            time.sleep(self.sleepTime)
            if hasattr(self.callBack, '__call__'):
            	self.callBack()
            else: 
            	print 'Can\'t execute callBack'