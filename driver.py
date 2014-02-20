import serial


class Driver:
	"""docstring for driver"""
	def __init__(self):
		self.ser = serial.Serial('/dev/tty.usbmodem1421', 9600)
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
		print 'Serial connected'

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
		# return self.queryData(self.ALL_INFO)

	def startWatering(self):
		self.ser.write(self.greenColor)

	def stopWatering(self):
		self.ser.write(self.redColor)

	def queryData(self, arg):
		self.ser.write(arg)
		outPut = ""
		while outPut == "":
			outPut = self.ser.readline()
		return outPut

