import glob
import os
import string
import pandas as pd

def getBasename(files):
	''' this is built in to work even if the basename contains .
	'''
	files = [('.').join(x.split(os.sep)[-1].split('.')[:-1]) for x in files]
	return files

def randomName(lengthStr=8, withString=False):
	''' function to generate random number or string
	lengthStr: integer correspond to the lenght of the password
	withString: logical determine if the random name is goign to be 
	'''
	nums = string.digits
	randName = ''.join(nums[c % len(nums)] for c in os.urandom(lengthStr))

	if withString == True:
		chars = string.ascii_letters + string.digits + '+/'
		assert 256 % len(chars) == 0  # non-biased later modulo
		randName = ''.join(chars[c % len(chars)] for c in os.urandom(lengthStr))

	return randName

def correspondingTable(files):
	'''
	list of fiels
	'''
	dt = pd.DataFrame({'originFull':files})
	dt['basename'] = dt.apply(lambda x: getBasename(x))
	dt['newName'] = dt.apply(lambda x: randomName(), axis=1)
	storepath = os.path.dirname(files[0])
	storeName = storepath+os.sep+'corresp.pkl'
	dt.to_pickle(storeName)
	
	print('Correspondance binary store here: ', storeName)
	return dt

def anonymize(path):
	'''
	this function will find all the files in the path that contains the reference name
	and will make the file anaonymous
	'''
	for i, j in dt.iterrows():
		# print(j['basename'])
		allFiles = glob.glob(path+'/**/*'+j['basename']+'*', recursive=True)

		for k in allFiles:
			newk = k.replace(j['basename'], '__'+j['newName']+'__')
			# print(k)
			# print(newk)
			os.rename(k, newk)

## Example Usage
path = r'C:\Users\Windows\Desktop\test'
files = glob.glob(path+os.sep+'*.avi')
dt = correspondingTable(files)
anonymize(path)

# to read back the correspondence
lo = pd.read_pickle(path+os.sep+'corresp.pkl')