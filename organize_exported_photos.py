import sys
import os

class FileWrapper:
	name = None
	path = None
	dirPath = None
	extension = None

	def __init__(self, dirEntryObj):
		self.name, self.extension = os.path.splitext( os.path.basename(dirEntryObj.path) )
		self.path = dirEntryObj.path
		self.dirPath = os.path.dirname(dirEntryObj.path)

	def move(self, newPath):
		os.rename( self.path, str(newPath + self.extension) )

	def rename(self, newName):
		pass



PATH = None

def main():
	if(len(sys.argv) > 1):
		print(sys.argv[1])
		PATH = sys.argv[1]
	else:
		# print(os.getcwd())
		PATH = os.getcwd()
	
	PATH = os.getcwd() + '/Fotos/'
	filesList = os.scandir(PATH)

	for file in filesList:
		# print( file.name )
		if( os.path.isdir(file.path) ):
			splittedName = file.name.split(',')
			year = splittedName[-1].strip()
			# print( year )
			# print( PATH + year )


			if( not os.path.isdir(PATH + year) ):
				splittedName.pop()
				# os.mkdir(PATH + year)
				print( splittedName )




		# file = FileWrapper(file)
		# newPath = str(file.dirPath + '/copy2')
		# file.move( newPath )

	# print(os.listdir(PATH));


# Get file name only, without extension
def getFileName(absPath):
	return os.path.splitext( os.path.basename(absPath) )[0]



main()