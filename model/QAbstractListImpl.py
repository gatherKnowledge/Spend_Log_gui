from PyQt5.QtCore import QAbstractListModel




class QAbstractListImpl(QAbstractListModel):
	def __init__(self, data=None, parent=None):
		QAbstractListModel.__init__(self, parent)
		self._data = data

	# getter
	def get_data(self):
		return self._data

	# getter
	def set_data(self, data):
		self._data = data

