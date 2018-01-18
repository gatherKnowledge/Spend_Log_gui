class ListAddTest:
	def __init__(self):
		self.my_data = 'this is my data'
	def print_mydata(self):
		print(self.my_data)

l = list()
obj = ListAddTest()
l.append(obj)
l[0].print_mydata()
