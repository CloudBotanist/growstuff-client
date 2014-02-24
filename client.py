from socketIO_client import SocketIO, BaseNamespace
import logging, time

from driver import Driver
from uuid import getnode as get_mac
# logging.basicConfig(level=logging.DEBUG)

def getID():
	f = open('plant.conf', 'r')
        id = f.read().replace('\n', ' ').replace('\r', '').replace(' ', '')	
	return '{"id": "' + id + '"}'

def getStatus():
	jsonInfo = arduino.readAllInfo()
 	print jsonInfo
 	return jsonInfo

class Namespace(BaseNamespace):

	def on_connection_succeed(self, *args):
		print 'Connection succeeded'

	def on_watering(self, *args):
		print "---> Server asked for watering"
		wateringTime = int(args[0])
		arduino.waterWithDuration(wateringTime)

	def on_picture(self, *args):
		print "Take a picture !"

socketIO = SocketIO('http://growstuff.herokuapp.com', 80, Namespace)

arduino = Driver();
arduino.setSerial()

socketIO.emit("identification", getID())
time.sleep(2)

while 1:
	socketIO.emit('status', getStatus())
	socketIO.wait(seconds=60)
