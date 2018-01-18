import os
from utils import Constant as const
from model.Product import Product

def check_input(value):
	try:
		i = int(value)
		return i
	except ValueError as vError:
		return 0
	# return void : int
	#        except :

# 무조건 한 큐에 정리할 것
def save_file(fileName, pList):
	fdir =  const.PATH + fileName + const.EXT
	string = str()
	for rs in pList :
		string = string + rs.stringize()
	# f = open(fdir, 'w', encoding=const.En_TYPE)
	f = open(fdir, 'w', encoding=const.En_TYPE)
	f.write(string)
	f.close()

def read_directory(dirPath):
	for root, dirs, files in os.walk('./'):
		for file in files:
			print(file)


def read_file(fileName):
	fdir =  const.PATH + fileName + const.EXT
	f = open(fdir, encoding=const.En_TYPE)
	rList = list()
	for line in f.readlines() :
		rList.append(line)
		print(line)
	return rList

if __name__=='__main__':
	obj = Product('1', '1', '1', '1', '1', '1801011212')
	# save_file(obj)

