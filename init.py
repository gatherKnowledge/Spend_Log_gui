import sys
import datetime
import utils.Util as util
from utils import Constant as const

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTime
from model.Product import Product



global_list_product = list()
global_list_chart = list()

form = uic.loadUiType("./ui/spend_log.ui")[0]

"""
* Rules
 함수 명명할 때, 유저 동작과 관계돼 있는 이벤트들은 접미사에 '~_event'
 
* 추가 기능 
 [v] 1. 파일 만들어서 관리
 2. 파일 로드
 3. 차트화 
 4. 세팅파일 생성
 [v] 5. 매수,매도 목록에 시간 표기
"""


class UiMain(QMainWindow, form):
	def __init__(self):

		super().__init__()
		# 화면 로드
		self.setupUi(self)
		# Events 등록
		self.load_events()
		# Value 추가
		self.load_data()

	def load_data(self):
		self.lineAmount.setText('0')
		self.lineCost.setText('0')

	def load_events(self):
		"""
		메인 이벤트 기능
		"""
		# 기본값 고정 버튼
		self.checkDefault.clicked.connect(self.enable_time_event)
		# list 클릭 시 이벤트
		self.listProduct.clicked.connect(self.detail_view_event)
		# list 클릭 시 이벤트
		self.listFile.clicked.connect(self.file_view_event)
		# 입력필드 정보 목록으로 이동
		self.btnAdd.clicked.connect(self.add_list_event)
		# 라벨 값 테스트
		self.btnDelete.clicked.connect(self.delete_list_event)
		# 파일 생성 버튼
		self.btnMakeFile.clicked.connect(self.save_list)
		# 탭 버튼 클릭 시
		self.tabWidget.tabBarClicked.connect(self.load_log)
		# 챠트 보기
		self.btnOutput.clicked.connect(self.load_chart)
		# 파일 삭제
		self.btnDfile.clicked.connect(self.delete_file_event)

		"""
		+5/-5 button time event 
		"""
		self.btnPlusTime.clicked.connect(self.plus_time)
		self.btnMinusTime.clicked.connect(self.minus_time)

		"""
		+5/-5 button value event 
		"""
		self.btnPlusCost.clicked.connect(self.plus_cost)
		self.btnMinusCost.clicked.connect(self.minus_cost)
		self.btnPlusAmount.clicked.connect(self.plus_amount)
		self.btnMinusAmount.clicked.connect(self.minus_amount)

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
	def plus_time(self):
		present = self.editTime.time()
		hour = present.hour()
		minute = present.minute()
		minute = util.calulate_plus(minute)
		after_time = QTime(hour, minute)
		self.editTime.setTime(after_time)

	def plus_cost(self):
		value = self.lineCost.text()
		value = int(value) + 5
		self.lineCost.setText(str(value))

	def plus_amount(self):
		value = self.lineAmount.text()
		value = int(value) + 5
		self.lineAmount.setText(str(value))

	def minus_time(self):
		present = self.editTime.time()
		hour = present.hour()
		minute = present.minute()
		minute = util.calulate_minus(minute)
		after_time = QTime(hour, minute)
		self.editTime.setTime(after_time)

	def minus_cost(self):
		value = self.lineCost.text()
		value = int(value) - 5
		self.lineCost.setText(str(value))

	def minus_amount(self):
		value = self.lineAmount.text()
		value = int(value) - 5
		self.lineAmount.setText(str(value))

	def load_chart(self):
		x_sell = list()
		x_buy = list()
		y_sell = list()
		y_buy = list()
		dct_buy = dict()
		dct_sell = dict()

		for prdt_str in global_list_chart :
			splited = prdt_str.split(',')
			if splited[2] == '매수' :
				tmp = splited[0]
				x_value = tmp[6:]
				y_value = splited[3]
				try:
					dct_buy[x_value] = int(dct_buy[x_value]) + int(y_value)
				except KeyError:
					dct_buy[x_value] = int(y_value)

			elif splited[2] == '매도' :
				tmp = splited[0]
				x_value = tmp[6:]
				y_value = splited[3]
				try:
					dct_sell[x_value] = int(dct_sell[x_value]) + int(y_value)
				except KeyError:
					dct_sell[x_value] = int(y_value)

		for k in dct_buy.keys():
			x_buy.append(k)
		for v in dct_buy.values():
			y_buy.append(v)

		for k in dct_sell.keys():
			x_sell.append(k)
		for v in dct_sell.values():
			y_sell.append(v)



		j = len(dct_buy.keys())
		while j :
			for i,k in enumerate(x_buy) :
				try:
					if x_buy[i] > x_buy[i+1] :
						tmp = x_buy[i]
						x_buy[i] = x_buy[i+1]
						x_buy[i+1] = tmp

						tmp = y_buy[i]
						y_buy[i] = y_buy[i + 1]
						y_buy[i + 1] = tmp
				except Exception :
					pass
			j = j-1
		j = len(dct_sell.keys())
		while j:
			for i, k in enumerate(x_sell):
				try:
					if x_sell[i] > x_sell[i + 1]:
						tmp = x_sell[i]
						x_sell[i] = x_sell[i + 1]
						x_sell[i + 1] = tmp

						tmp = y_sell[i]
						y_sell[i] = y_sell[i + 1]
						y_sell[i + 1] = tmp
				except Exception:
					pass
			j = j - 1

		print('x')
		print(x_buy)
		print(y_buy)

		print('y')
		print(x_sell)
		print(y_sell)


		util.config_chart('Time', 'Amount', 'y', 'Total')
		util.set_line(x_buy, y_buy, label_name='매수', color='r')
		util.set_line(x_sell, y_sell, label_name='매도', color='b')
		util.show_chart()

		# self.value_event_impl(str(self.comboKind.currentText()))
		# self.value_event_impl(str(self.comboBuySell.currentText()))
		# self.value_event_impl(str(self.textDesc.toPlainText()))
	def load_log(self, retFlag=None):
		print(self.tabWidget.currentIndex())
		if self.tabWidget.currentIndex() is 1 and retFlag :
			return

		rList = util.read_directory(const.PATH)
		view = self.listFile
		view.clear()
		for file_name in rList :
			item = QListWidgetItem(view)
			item.setText(file_name)


	def analize_log(self, fileName):
		# [.]로 분리된 파일
		global_list_chart.clear()

		for strPrd in util.read_file(fileName) :
			global_list_chart.append(strPrd)
			# strPrd.split(',')


	def file_view_event(self):
		view = self.listFile
		self.analize_log(view.currentItem().text())



	def detail_view_event(self):
		view = self.listProduct
		# self.labelDetail.setText()
		tmp = global_list_product[view.currentRow()].make_str()
		self.labelDetail.setText(tmp)

	def delete_file_event(self):
		view = self.listFile
		fileName = view.currentItem().text()
		util.delete_file(fileName)
		self.load_log(retFlag=0)

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
			pTime = self.editTime.dateTime().toString('hhmm')
		elif self.checkDefault.checkState() == 2 :
			pTime  = date.strftime('%H%M')
		rTime = preDate + pTime

		p = Product(name=pname, yongdo=pyongdo, yang=pyang,dec=pdec, price=pprice,time=rTime)
		global_list_product.append(p)
		view = self.listProduct
		item = QListWidgetItem(view)
		item.setText('('+str(pTime)[:2]+':' +str(pTime)[2:]+') '+str(p.name) + '/' + str(p.yongdo))

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

	#
	def save_list(self):
		date = datetime.datetime.now()
		reply = QMessageBox.question(self, "알림"
		                             , "파일을 만드시겠습니까?", QMessageBox.Yes | QMessageBox.No)
		if reply == QMessageBox.No:
			return
		if len(global_list_product) is not 0 :
			util.save_file(date.strftime('%y%m%d'), global_list_product)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ui = UiMain()
	ui.show()
	app.exec_()