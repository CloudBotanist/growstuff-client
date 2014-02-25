from socketIO_client import SocketIO, BaseNamespace
import logging, time

from driver import Driver
#logging.basicConfig(level=logging.DEBUG)

def getID():
	f = open('plant.conf', 'r')
        id = f.read().replace('\n', ' ').replace('\r', '').replace(' ', '')	
	jsonID =  '{"id":"' + id + '"}'
	print jsonID
	return jsonID

def getStatus():
	jsonInfo = arduino.readAllInfo()
 	print jsonInfo
 	return jsonInfo

def waitForConnection():
	while 1:
		try:
			socket = SocketIO('http://growstuff.herokuapp.com', 80, Namespace)
			return socket	
		except:
			#let's try again in a few
			time.sleep(60)						
	# When connected
	socketIO.emit("identification", getID())
	time.sleep(2)
	#print 'Server connected!'

class Namespace(BaseNamespace):

	def on_connection (self, *args):
		print 'Server connected!'
	def on_disconnection(self, *args):
		
		print 'Server disconnected!'

	def on_watering(self, *args):
		print '---> Server asked for watering'
		wateringTime = int(args[0])
		arduino.waterWithDuration(wateringTime)

	def on_picture(self, *args):
		print '---> Take a picture !'


print 'Connecting to the Server...'
socketIO = waitForConnection()

print 'Connecting to the Arduino...'
arduino = Driver();
arduino.setSerial()
print 'Arduino connected!'



try:
	socketIO.emit('status', getStatus())
	socketIO.wait(seconds=60)
except:
	print "Lost connection: waiting for reconnection"
	socketIO = waitForConnection()
