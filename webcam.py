from dropbox.client import DropboxClient, DropboxOAuth2FlowNoRedirect
import os, subprocess, datetime

ACCES_TOKEN = 'F3IBRMPc3KkAAAAAAAAAAQr-RHJVtEj-6u4jG7aOO6fMIjkSX9YV8T5UmudaxciD'
PICTURE_CMD = 'fswebcam -d /dev/video0 -r 640x480 '
REMOVE_CMD = 'sudo rm -f '

class Webcam:	
	    
	def __init__(self, plantId):
		self.plantId = plantId
           
   	def takePicture(self):
		self.client = DropboxClient(ACCES_TOKEN)
		print self.client.account_info()

       		name = datetime.datetime.now().strftime("%y-%m-%d-%H-%M") + '.jpg'
		command = PICTURE_CMD + name
		process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)        	
		process.wait()
       		response = self.client.put_file(self.plantId + '/' + name, open(name, 'r'))
		os.remove(name)
