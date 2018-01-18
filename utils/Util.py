import os
from model.Product import Product

"""
Constant
"""
PATH = './data/'
EXT = '.etf'

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
	dir =  PATH + fileName + EXT
	# if os.path.exists(dir) :
	# 	print("EXIST")
	# else:
	# 	print("NOT EXIST")
	string = str()
	for rs in pList :
		string = string + rs.stringize()
	f = open(dir, 'w', encoding="utf-8")
	f.write(string)


if __name__=='__main__':
	obj = Product('1', '1', '1', '1', '1', '1801011212')
	# save_file(obj)

