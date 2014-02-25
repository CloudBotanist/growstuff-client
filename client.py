from socketIO_client import SocketIO, BaseNamespace
import logging, time

from driver import Driver
# logging.basicConfig(level=logging.DEBUG)

def getID():
	f = open('plant.conf', 'r')
        id = f.read().replace('\n', ' ').replace('\r', '').replace(' ', '')	
	return '{"id": "' + id + '"}'

def getStatus():
	jsonInfo = arduino.readAllInfo()
 	print jsonInfo
 	return jsonInfo

def waitForConnection():
	isConnected = False;
	while not isConnected:
		try:
			socketIO = SocketIO('http://growstuff.herokuapp.com', 80, Namespace)
			isConnected = True
		except Exception, e:
			print 'Socket disconnected'
			isConnected = False
	# When connected
	socketIO.emit("identification", getID())
	time.sleep(2)

class Namespace(BaseNamespace):

	def on_connection_succeed(self, *args):
		print 'Connection succeeded'

	def on_watering(self, *args):
		print "---> Server asked for watering"
		wateringTime = int(args[0])
		arduino.waterWithDuration(wateringTime)

	def on_picture(self, *args):
		print "Take a picture !"

socketIO = None
waitForConnection()

arduino = Driver();
arduino.setSerial()


while 1:
	try:
		socketIO.emit('status', getStatus())
		socketIO.wait(seconds=60)
	except:
		waitForConnection()
