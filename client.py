from socketIO_client import SocketIO, BaseNamespace
import logging, json

from driver import Driver
from uuid import getnode as get_mac
# logging.basicConfig(level=logging.DEBUG)

nb_status = 0

def readableMACaddress():
	# return '-'.join('%02X' % ((get_mac() >> 8*i) & 0xff) for i in reversed(xrange(6)))
	return "5306f1a014b36602009d423c"

def status():
	jsonID = '{"tmp": 18, "hum": 56, "light": 80, "ground_hum": 95, "water_presence": false}'
	# tempStatus = arduino.readAllInfo()
	# jsonID = '{"tmp":'+tempStatus.get('tmp')+', "hum":'+tempStatus.get('hum')+', "light":'+tempStatus.get('light')+', "ground_hum":'+tempStatus.get('ground_hum')+', "water_presence": false}'
	return jsonID

def jsonID():
	return '{"id": "' + readableMACaddress() + '"}'

class Namespace(BaseNamespace):

	def on_connection_succeed(self, *args):
		print 'Conenction succeed'

	def on_watering(self, *args):
		print "---> Server asked for watering"
		wateringTime = int(args[0])
		arduino.waterWithDuration(wateringTime)

	def on_picture(self, *args):
		print "Take a picture !"

socketIO = SocketIO('http://growstuff.herokuapp.com', 80, Namespace)

arduino = Driver();
arduino.setSerial()

socketIO.emit("identification", jsonID())

while 1:
	socketIO.emit('status', status())
	socketIO.wait(seconds=20)
	print status()
	nb_status += 1
