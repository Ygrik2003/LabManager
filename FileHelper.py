

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
	def __init__(self, path : str, rows : int, columns : int, is_open=False):
		'''
		path - path to file, which keep you data
		rows - count rows of matrix in file
		columns - count columns of matrix in file
		is_open - sets whether the default file will be opened
		'''
		self.openFile(path)
		self.setSize(rows, columns)

		if is_open:
			self.file = open(self.path, 'r')

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
		#TODO
		return inData

	def readOutData(self, startOut : tuple, endOut : tuple):
		'''
		startOut - left top indexes of output matrix data
		endOut - right bottom indexes of output matrix data
		'''
		outData = []
		#TODO
		return outData

	def openFile(self, path : str, isOpen=False):
		'''
		path - path to file, which keep you data
		is_open - sets whether the default file will be opened
		'''
		self.pathToFile = path

		if is_open:
			self.file = open(self.path, 'r')

	def setSize(self, rows : int, columns : int):
		'''
		rows - count rows of matrix in file
		columns - count columns of matrix in file
		'''
		self.rows = rows
		self.columns = columns