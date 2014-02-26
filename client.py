from socketIO_client import SocketIO, BaseNamespace
from driver import Driver
import logging, time

#logging.basicConfig(level=logging.DEBUG)

firstConnection = False

class Namespace(BaseNamespace):

	def on_connect (self):
		print '---> Server connected!'
		global firstConnection
		firstConnection = True
		self.emit("identification", getID())
		
	def on_disconnect(self):
		print '---> Server disconnected!'
		connected = false

	def on_watering(self, *args):
		print '---> Server asked for watering'
		wateringTime = int(args[0])
		arduino.waterWithDuration(wateringTime)

	def on_picture(self, *args):
		print '---> Take a picture!'

def getID():
	f = open('plant.conf', 'r')
    	ID = f.read().replace('\n', ' ').replace('\r', '').replace(' ', '')	
	print 'ID: ' + ID
	return '{ "id": "' + ID + '" }'

def getStatus():
	jsonInfos = arduino.readAllInfos()
 	print 'Status: ' + jsonInfos
 	return jsonInfos

print 'Connecting to the Arduino...'
arduino = Driver();
arduino.init()
print '---> Arduino connected!'
	        
print 'Connecting to the Server...'
socketIO = SocketIO('growstuff.herokuapp.com', 80, Namespace)

while not firstConnection:
	socketIO.wait(seconds=1)
while 1: 
	socketIO.emit('status', getStatus())
	socketIO.wait(seconds=60)
