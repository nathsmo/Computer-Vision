class VideoCaptureThread:
	""" Threaded VideoCapture from cv2
	"""

	def __init__(self, src=0): # src = fuente
		self.cap = cv.VideoCapture(src)
		self.ret, self.frame = self.cap.read()
		self.stopped = Flase

	def start(self):
		#create thread and start executing
		Thread(targat=self.capture, args=()).start()
		return self

	def capture(self):
		while not self.stopped:
			if not self.ret:
				self.stop()
			else:
				self.ret, self.frame - self.cap.read()

	def stop(self)
		self.stopped = True