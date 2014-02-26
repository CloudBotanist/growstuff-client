import serial, json
from asyncSleep import AsyncSleep


class Driver:
	"""docstring for driver"""
	def __init__(self):
		self.WATER_ON = '\x00'
		self.WATER_OFF = '\x01'
		self.TEMPERARTURE_CMD = '\x02'
		self.HUMIDITY_CMD = '\x03'
		self.LIGHT_CMD = '\x04'
		self.SOIL_COMMAND = '\x05' 
		self.WATER_INFO = '\x06'
		self.ALL_INFO = '\x07'

	def init(self, url='/dev/ttyACM0', baudrate=9600):
		try:
			self.ser = serial.Serial(url, baudrate, timeout=3)
			print 'Serial connected'
		except OSError:
			print('Can\'t connect to hardware')

	def diconnect(self):
		self.ser.close()

	def readHumidity(self):
		return self.queryData(self.HUMIDITY_CMD)

	def readTemperature(self):
		return self.queryData(self.TEMPERARTURE_CMD)

	def readLight(self):
		return self.queryData(self.LIGHT_CMD)

	def readSoilHumidity(self):
		return self.queryData(self.SOIL_COMMAND)

	def readWaterLevel(self):
		return self.queryData(self.WATER_INFO)

	def readAllInfos(self):
		infos = self.queryData(self.ALL_INFO).split('|')
                infoJson = json.dumps({
                        "tmp": int(infos[0]),
                        "hum": int(infos[1]),
                        "light": int(infos[2]),
                        "ground_hum": int(infos[3]),
                        "water_presence": int(infos[4])
                })
                return infoJson

	def startWatering(self):
		print "---> Start watering"
		self.pushData(self.WATER_ON)

	def stopWatering(self):
		print "---> Stop watering"
		self.pushData(self.WATER_OFF)

	def waterWithDuration(self, waterTime):
		self.startWatering()
		sleep = AsyncSleep(waterTime, self.stopWatering)
		sleep.start()

	def queryData(self, arg):
		if hasattr(self, 'ser'):
			try:
				self.ser.write(arg)
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
