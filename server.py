
import sys
import socket
import time
import threading
import base64

class mirror():
	def text(custom_string):

		try:
			print(str(custom_string))
			return
		except OSError as exp:
			return

class socketIO():
	def __init__(self,port):
		self.port = port
		self.con = None
		self.lock = threading.Lock()
		self.thread_2 = threading.Thread(name='ioThread', target=self.run, daemon=False)
		self.stop_thread = False

	def start(self):
		self.socketThreadRunning = True
		self.thread_2.start()

	def Disconnect(self):
		self.socketThreadRunning = False
		self.con.close()

	def Connect(self):
		sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		sock.bind(('',self.port))
		sock.listen(1)
		try:
			(self.con,address) = sock.accept()
			mirror.text("(+) Connected.\r\n")

		except socket.error as e:
			mirror.text("(-) Not Connected. ")
			mirror.text(" Socket Error: " + str(e))

		return self.con

	def run(self):
        self.socketThreadRunning = True
        time.sleep(.001)
        while self.socketThreadRunning == True:
        	#emokit thing
