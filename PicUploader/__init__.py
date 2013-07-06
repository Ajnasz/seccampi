import requests
class PicUploader:
	host = '192.168.1.2'
	port = '3000'
	path = '/pic'
	def __init__(self):
		return

	def upload(self, file_path):
		files = {'file': ('file.jpg', open(file_path, 'rb'))}
		request = requests.put('http://' + self.host + ':' + self.port + self.path, files = files)
		print(request.content)
		

