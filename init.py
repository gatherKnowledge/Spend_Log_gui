import sys
import datetime
import util

from PyQt5 import uic
from PyQt5.QtWidgets import *
from model.Product import Product


global_list_product = list()
form = uic.loadUiType("./ui/spend_log.ui")[0]

"""
* Rules
 함수 명명할 때, 유저 동작과 관계돼 있는 이벤트들은 접미사에 '~_event'
 
* 추가 기능 
 1. 파일 만들어서 관리
    * Json타입으로 개발
    * 
 2. 
 
"""

class UiMain(QMainWindow, form):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		# 기본값 고정 버튼
		self.checkDefault.clicked.connect(self.enable_time_event)

		# list 클릭 시 이벤트
		self.listProduct.clicked.connect(self.detail_view_event)

		# 입력필드 정보 목록으로 이동
		self.btnAdd.clicked.connect(self.add_list_event)

		# 라벨 값 테스트
		self.btnDelete.clicked.connect(self.delete_list_event)


		# 종료버튼
		self.btnClose.clicked.connect(self.close_event)


	"""
		TEST
	"""
	# test method value check
	def delete_list_event(self):
		view = self.listProduct
		row = view.currentRow()

		if row is -1 :
			return

		view.takeItem(row)
		global_list_product.pop(row)
		self.labelDetail.setText('')
		# self.value_event_impl(self.editTime.dateTime().toString('hhmm'))

		# checked : 2 / not checked : 0
		# self.value_event_impl(str(self.checkDefault.checkState()))

		# self.value_event_impl(str(self.comboKind.currentText()))
		# self.value_event_impl(str(self.comboBuySell.currentText()))
		# self.value_event_impl(str(self.textDesc.toPlainText()))


	def detail_view_event(self):
		view = self.listProduct
		# self.labelDetail.setText()
		tmp = global_list_product[view.currentRow()].make_str() 
		self.labelDetail.setText(tmp)

	# test method value check
	def value_event_impl(self, string):
		# self.labelTest.setText(string)
		pass

	def add_list_event(self):
		# param : name, yongdo, yang, dec, price, time
		pprice = util.check_input(self.lineCost.text())
		pyang = util.check_input(self.lineAmount.text())
		if (pprice is 0) or (pyang is 0) :
			QMessageBox.question(self, "입력오류"
			                     , "입력형식 오류", QMessageBox.Yes)
			return
		pname =	self.comboKind.currentText()
		pyongdo = self.comboBuySell.currentText()
		pdec = self. textDesc.toPlainText()
		# 기존 값 체크가 안 되어 있는 경우

		date = datetime.datetime.now()
		preDate = date.strftime('%y%m%d')

		if self.checkDefault.checkState() == 0 :
			ptime = self.editTime.dateTime().toString('hhmm')
		elif self.checkDefault.checkState() == 2 :
			ptime  = date.strftime('%H%M')
		ptime = preDate + ptime

		p = Product(name=pname, yongdo=pyongdo, yang=pyang,dec=pdec, price=pprice,time=ptime)
		global_list_product.append(p)
		view = self.listProduct
		item = QListWidgetItem(view)
		item.setText(str(p.name) + '/' + str(p.yongdo))

	# 공통적으로 타겟에 대한 정보를 전달해 줄 수는 없을까?
	def enable_time_event(self):
		# target
		if self.editTime.isEnabled() is True :
			self.editTime.setEnabled(False)
		else :
			self.editTime.setEnabled(True)

	def close_event(self):
		reply = QMessageBox.question(self, "종료 알림"
		                             , "정말 종료 하시겠습니까?", QMessageBox.Yes | QMessageBox.No)
		if reply == QMessageBox.Yes:
			qApp.exit()
		else:
			pass


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ui = UiMain()
	ui.show()
	app.exec_()