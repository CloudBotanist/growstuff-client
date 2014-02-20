from socketIO_client import SocketIO, BaseNamespace
from multiprocessing import Pool
import logging, time, threading
from driver import Driver
from uuid import getnode as get_mac
logging.basicConfig(level=logging.DEBUG)

nb_status = 0

def readableMACaddress():
	return '-'.join('%02X' % ((get_mac() >> 8*i) & 0xff) for i in reversed(xrange(6)))

def on_server_call(*args):
	print 'Server sent: ', args
	response = '{"mac_address": "' + readableMACaddress() + '"}'
	print 'Respond: ', response
	socketIO.emit("identification", response)

def status():
	jsonID = '{"mac_address": "' + readableMACaddress() + '", "status":' + str(nb_status) +'}'
	return jsonID

def kiki():
	arduino.stopWatering()

class Namespace(BaseNamespace):

	def on_identification_query(self, *args):
		print 'Identification query : ', args
		response = '{"mac_address": "' + readableMACaddress() + '"}'
		socketIO.emit("identification", response)
		arduino.readAllInfo()

	def on_connection_succeed(self, *args):
		print 'Conenction succeed'

	def on_watering(self, *args):
		wateringTime = int(args[0])
		arduino.startWatering()
		# pool = Pool(processes=2) # Start a worker processes.
		# result = pool.apply_async(time.sleep(int(args[0])), [], arduino.stopWatering()) # Evaluate "f(10)" asynchronously calling callback when finished.
		threading.Timer(wateringTime, kiki()).start()
		# time.sleep(1)
		# arduino.push('\x00\x00\x00')

	def on_picture(self, *args):
		print "Take a picture !"

# socketIO = SocketIO('localhost', 8000, Namespace)
socketIO = SocketIO('http://growstuff.herokuapp.com', 80, Namespace)
# socketIO.set('transports', ['xhr-polling']);
# socketIO.set('polling duration', 10);

arduino = Driver();

jsonID = '{"mac_address": "' + readableMACaddress() + '"}'
socketIO.emit("identification", readableMACaddress())
# socketIO.wait(seconds=1000)

while 1:
	socketIO.wait(seconds=20)
	socketIO.emit('status', status())
	nb_status += 1
