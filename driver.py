import serial
from asyncSleep import AsyncSleep


class Driver:
	"""docstring for driver"""
	def __init__(self):
		self.greenColor = '\x00\xff\x00'
		self.blueColor = '\x00\x00\xff'
		self.redColor = '\xff\x00\x00'
		self.colors = [self.redColor, self.greenColor, self.blueColor]
		self.WATER_ON = '\x00'
		self.WATER_OFF = '\x01'
		self.TEMPERARTURE_CMD = '\x02'
		self.HUMIDITY_CMD = '\x03'
		self.LIGHT_CMD = '\x04'
		self.SOIL_COMMAND = '\x05' 
		self.WATER_INFO = '\x06'
		self.ALL_INFO = '\x07'

	def setSerial(self, url='/dev/tty.usbmodem1421', port=9600):
		try:
			self.ser = serial.Serial(url, port)
			print 'Serial connected'
		except OSError:
			print('Can\'t connect to hardware')

	def close(self):
		self.ser.close()

	def push(self, data):
		self.ser.write(data)

	def pop(self, bufferSize):
		return self.ser.readline()

	def readHumidity(self):
		return self.queryData(self.HUMIDITY_CMD)

	def readTemperature(self):
		return self.queryData(self.TEMPERARTURE_CMD)

	def readLight(self):
		return self.queryData(self.LIGHT_CMD)

	def readSolHumidity(self):
		return self.queryData(self.SOIL_COMMAND)

	def readWaterLevel(self):
		return self.queryData(self.WATER_INFO)

	def readAllInfo(self):
		self.ser.write(self.blueColor)

	def startWatering(self):
		print "---> Start watering"
		self.pushData(self.greenColor)

	def stopWatering(self):
		print "---> Stop watering"
		self.pushData(self.redColor)

	def waterWithDuration(self, waterTime):
		self.startWatering()
		sleep = AsyncSleep(waterTime, self.stopWatering)
		sleep.start()

	def queryData(self, arg):
		if hasattr(self, 'ser'):
			try:
				self.ser.write(arg)
				outPut = ""
				while outPut == "":
					outPut = self.ser.readline()
				return outPut
			except OSError:
				print('Can\'t connect to hardware')
		else:
			print "Hardware not connected"

	def pushData(self, arg):
		if hasattr(self, 'ser'):
			try:
				self.ser.write(arg)
			except OSError:
				print('Can\'t connect to hardware')
		else:
			print "Hardware not connected"

		

