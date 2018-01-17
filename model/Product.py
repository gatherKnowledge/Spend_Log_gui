import datetime
import json

class Product():
	def __init__(self, name, yongdo, yang, dec, price, time):
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
		strn = '\n'
		strn += self.time
		strn += '\n\''+self.name + '\'을/를 '+ format(int(self.price), ",") +'에 ' + format(int(self.yang), ",") + '개 ' + self.yongdo + '했습니다.'
		strn += '\n비고 : '+ self.dec
		strn += '\n총 '+ self.yongdo +' 금액' + format(int(self.total_price), ",") + '원'
		return strn

	def print_obj(self):
		strn = self.make_str()
		print(strn)

	# json style object data
	def getInstanceJson(self):
		test = vars(self)
		return json.dumps(test)