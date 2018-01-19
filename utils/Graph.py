import matplotlib.pyplot as plt
from utils import Util

class Graph:
	def __init__(self):
		pass
		"""
		plt.plot([1, 2, 3, 4])
		"""
		"""
		x = range(0, 100)
		y = [v * v for v in x]
		plt.plot(x, y)
		"""

	# param : json type
	# def detach_data(self, param_prduct):
	# 	param_prduct.

	def set_line(self, x, y, label_name = None):
		# plt.plot(['12:31', '12:41', '13:31', '15:31'] , [1, 2, 3, 4], label='sell')
		plt.plot(x , y, 's--',label=label_name)
		plt.scatter(x, y)

	def show_chart(self):
		plt.show()

	def hover_mouse(self):
		pass

	def config_chart(self, xlabel, ylabel, grid, title=None):

		plt.figure(figsize=(6,4))
		plt.xlabel(xlabel)
		plt.ylabel(ylabel)
		plt.title(title)

		if str(grid).lower() is 'y':
			plt.grid()

		plt.legend()



# gr = Graph()
# gr.set_line(['12:30'], [1])
# gr.hover_mouse()
# gr.show_chart()

"""
plt.annotate("여기가 0.5!", 
             xy=(t, np.cos(t)), xycoords='data', xytext=(-90, -50), 
             textcoords='offset points', 
             fontsize=16, arrowprops=dict(arrowstyle="->"))
"""
if __name__=='__main__':
	f = Util.read_file('180118')
	print(f)