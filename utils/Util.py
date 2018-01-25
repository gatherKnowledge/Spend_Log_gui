import os
from utils import Constant as const
from model.Product import Product
import matplotlib.pyplot as plt


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

# 경로에 존재하는 파일 목록 확인
def read_directory(dirPath):
	rList = list()
	for root, dirs, files in os.walk(dirPath):
		for file in files:
			# print(file)
			rList.append(file)
	return rList

# 파일 읽기/라인당 하나의 object
# return list
def read_file(fileName):
	fdir =  const.PATH + fileName
	f = open(fdir, encoding=const.En_TYPE)
	rList = list()
	for line in f.readlines() :
		rList.append(line)
	f.close()
	return rList

# 파일 삭제
def delete_file(fileName):
	fdir = const.PATH + fileName
	os.remove(fdir)


def calulate_plus(value):
	value = value + 5
	value = value % 60
	return value

def calulate_minus(value):
	value = value - 5
	if value < 0 :
		value = value + 60
	return value


"""
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Graph 그리기 관련 Util
Start
------------------------------------------------------------------------------------
"""
def set_line(x, y, label_name = None, color = 's'):
	# plt.plot(['12:31', '12:41', '13:31', '15:31'] , [1, 2, 3, 4], label='sell')
	plt.plot(x , y, color +'-',label=label_name)
	plt.scatter(x, y)

def show_chart():
	plt.show()

def config_chart(xlabel, ylabel, grid, title=None):

	plt.figure(figsize=(6,4))
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.title(title)

	if str(grid).lower() is 'y':
		plt.grid()

	plt.legend()
"""
------------------------------------------------------------------------------------
Graph 그리기 관련 Util
End
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
"""

if __name__=='__main__':
	obj = Product('1', '1', '1', '1', '1', '1801011212')
	# save_file(obj)

