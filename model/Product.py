import datetime
import json

class Product():
	def __init__(self, time, name, yongdo, yang, dec, price):
		self.name = name
		self.yongdo = yongdo
		self.yang = yang
		self.dec = dec
		self.time = time
		self.price = price
		self.total_price = int(yang) * int(price)

	def test(self):
		print('my string ')

	def make_str(self):
		# tmp = self.time.strftime('%y년 %m월 %일 %A\n%h%m')
		print
		# datetime.datetime.strptime("2017-01-02 14:44", "%Y-%m-%d %H:%M")
		tmp = self.time
		to_date = datetime.datetime.strptime(tmp, "%Y%m%d%H%M")

		# 18/01/17/0000
		print(tmp)
		# TODO dt.weekday()   {0:월, 1:화, 2:수, 3:목, 4:금, 5:토, 6:일}

		strn = '\n'
		strn += tmp[0:2]+'년 '+tmp[2:4]+'월 '+tmp[4:6]+'일 '+to_date.strftime("%A")[0:3]+' \n'+tmp[6:8]+'시'+tmp[8:10]+'분\n=>'
		strn += '\''+self.name + '\'을/를 '+ format(int(self.price), ",") +'에 ' + format(int(self.yang), ",") + '개 ' + self.yongdo + '했습니다.'
		strn += '\n비고 : '+ self.dec
		strn += '\n총 '+ self.yongdo +' 금액' + format(int(self.total_price), ",") + '원'
		return strn


	def print_obj(self):
		strn = self.make_str()
		print(strn)

	#
	def stringize(self):
		temp = self.time + ',' + self.name + ',' + self.yongdo + ',' + str(self.yang) + ',' + self.dec + ',' + str(self.price) + '\n'
		print(temp)
		return temp

	# json style object data
	def getInstanceJson(self):
		test = vars(self)
		return json.dumps(test)