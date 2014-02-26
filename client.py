from socketIO_client import SocketIO, BaseNamespace
from driver import Driver
from webcam import Webcam
import logging

#logging.basicConfig(level=logging.DEBUG)

class Namespace(BaseNamespace):

	def on_connect (self):
		print '---> Server connected!'
		global firstConnection, jsonId
		firstConnection = True
		self.emit("identification", jsonId)
		
	def on_disconnect(self):
		print '---> Server disconnected!'
		connected = false

	def on_watering(self, *args):
		print '---> Server asked for watering'
		wateringTime = int(args[0])
		arduino.waterWithDuration(wateringTime)

	def on_picture(self, *args):
		print '---> Server asked for a picture!'
		global plantId
		Webcam(plantId).takePicture()

def getId():
	f = open('plant.conf', 'r')
    	plantId = f.read().replace('\n', ' ').replace('\r', '').replace(' ', '')	
	print 'Plant ID is: ' + plantId
	return plantId	

def getStatus():
	jsonInfos = arduino.readAllInfos()
 	print 'Status: ' + jsonInfos
 	return jsonInfos

firstConnection = False
plantId = getId()
jsonId = '{"id":"'+ plantId + '"}'


print 'Connecting to the Arduino...'
arduino = Driver();
arduino.init()
print '---> Arduino connected!'
	        
print 'Connecting to the Server...'
socketIO = SocketIO('growstuff.herokuapp.com', 80, Namespace)
#socketIO = SocketIO('192.168.1.25', 8080, Namespace)

while not firstConnection:
	socketIO.wait(seconds=1)
while 1: 
	socketIO.emit('status', getStatus())
	socketIO.wait(seconds=60)
