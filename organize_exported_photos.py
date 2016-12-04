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



ROOT = None
obj = {}

def main():
	if(len(sys.argv) > 1):
		print(sys.argv[1])
		ROOT = sys.argv[1]
	else:
		# print(os.getcwd())
		ROOT = os.getcwd()
	
	ROOT = os.getcwd() + '/Fotos/'
	filesList = os.scandir(ROOT)

	for file in filesList:
		
		if( os.path.isdir(file.path) ):
			parsedPath = file.name.split(',')
			year = parsedPath[-1].strip()
			yearFolder = ROOT + year + '/'
			# print( year )
			print( yearFolder )
			if not year in obj:
				obj[year] = []

			if( not os.path.isdir(ROOT + year) ):
				parsedPath.pop()
				# os.mkdir(ROOT + year)

			day = parsedPath[-1].strip()
			dayFolder = yearFolder + day + '/'
			print( dayFolder )
			
			# compose obj and then add it? 
			if not day in obj[year]:
				obj[year] = { 'day': day, filesList: [] }

			photosList = os.listdir(file.path);
			for photo in photosList:
				# obj[year][fi]


		# file = FileWrapper(file)
		# newPath = str(file.dirPath + '/copy2')
		# file.move( newPath )

	# print(os.listdir(PATH));

	print( obj )


# Get file name only, without extension
def getFileName(absPath):
	return os.path.splitext( os.path.basename(absPath) )[0]



main()