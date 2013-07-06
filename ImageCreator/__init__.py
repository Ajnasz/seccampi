import time
import subprocess

class ImageCreator:

	IMAGE_FREQUENCY=45
	IMAGE_FOLDER="/storage/pic/"

	def __init__(self):
		self.last_img = 0;

	def createFilename(self):
		now = time.time()
		return self.IMAGE_FOLDER + "image-" + time.strftime("%Y%m%d%H%M%S") + ".jpg"

	def createImage(self):
		now = time.time()

		if (now - self.last_img >= self.IMAGE_FREQUENCY):
			# Record previous state
			fn = self.createFilename()
			subprocess.call(["/opt/vc/bin/raspistill", "-br", "65", "-o", fn]);
			self.last_img = now
			print("Image created at" + time.strftime("%Y-%m-%d %H:%M:%S") + ": " + fn)
			return fn
		else:
			return ''

