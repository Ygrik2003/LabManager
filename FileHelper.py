

class FileReader:
	''' 
		This class helped to you read data, if you have file with matrix of data and you need get input and output data.
		For example, you need parce this file
		1 1 1 3
		0 1 1 2
		1 1 0 2
		As input data you want get first 3 columns and as output - last column
		Then invoke readData() and give as params left top and right bottom indexes of input matrix data (in this case is (0, 0) and (2, 2))
		and left top and right bottom indexes of output matrix data (in this case is (3, 0) and (3, 2))
	'''
	def __init__(self, path : str, rows = 0, columns = 0):
		'''
		path - path to file, which keep you data
		rows - count rows of matrix in file
		columns - count columns of matrix in file
		'''
		self.openFile(path, is_open)
		self.setSize(rows, columns)
		self.data = list(map(split, self.file.readlines().split('\n')))

		for row in self.data:
			row = list(map(int, row))

		self.rows = len(self.data)
		if not self.rows:
			self.columns = len(self.data[0])
		else:
			print('ErrorMatrix') #Replace on Except


	def readData(self, startIn : tuple, endIn : tuple, startOut : tuple, endOut : tuple):
		'''
		startIn - left top indexes of input matrix data
		endIn - left bottom indexes of input matrix data
		startOut - left top indexes of output matrix data
		endOut - right bottom indexes of output matrix data
		'''
		inData, outData = [], []
		#TODO
		return inData, outData

	def readInData(self, startIn : tuple, endIn : tuple):
		'''
		startIn - left top indexes of input matrix data
		endIn - left bottom indexes of input matrix data
		'''
		inData = []

		for i in range(startIn[0], endIn[0] + 1):
			inData.append(self.data[i][startIn[1]:endIn[1] + 1])

		return inData

	def readOutData(self, startOut : tuple, endOut : tuple):
		'''
		startOut - left top indexes of output matrix data
		endOut - right bottom indexes of output matrix data
		'''
		outData = []

		for i in range(startOut[0], endOut[0] + 1):
			outData.append(self.data[i][startOut[1]:endOut[1] + 1])
		return outData

	def openFile(self, path : str):
		'''
		path - path to file, which keep you data
		'''
		self.pathToFile = path

	def setSize(self, rows : int, columns : int):
		'''
		rows - count rows of matrix in file
		columns - count columns of matrix in file
		'''
		self.rows = rows
		self.columns = columns

	def getData():
		return self.data