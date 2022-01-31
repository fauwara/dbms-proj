from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class UI_MainWindow(QMainWindow):
	def __init__(self):
		super(UI_MainWindow, self).__init__()
		self.setGeometry(800, 600, 800, 600)  # x, y, width, height
		self.setWindowTitle("DISTRIBUTOR 101")
		self.setupUi()

	def setupUi(self):
		
		self.guest_login = QtWidgets.QPushButton(self)
		self.guest_login.setGeometry(QtCore.QRect(320, 150, 200, 50))
		self.guest_login.setText("LOGIN AS GUEST")

		self.comboBox = QtWidgets.QComboBox(self)
		self.comboBox.setGeometry(QtCore.QRect(320, 320, 200, 30))
		self.comboBox.setStyleSheet("padding-left: 10px")
		self.comboBox.addItem("SUPPLIER")
		self.comboBox.addItem("RETAILER")
		self.comboBox.addItem("STAFF")
		
		self.line = QtWidgets.QFrame(self)
		self.line.setGeometry(QtCore.QRect(330, 210, 150, 20))
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		
		self.username_form = QtWidgets.QLineEdit(self)
		self.username_form.setGeometry(QtCore.QRect(320, 240, 200, 30))
		self.username_form.setStyleSheet("padding: 0px 10px")
		self.username_form.setPlaceholderText("PASSWORD")
		
		self.password_form = QtWidgets.QLineEdit(self)
		self.password_form.setGeometry(QtCore.QRect(320, 280, 200, 30))
		self.password_form.setStyleSheet("padding: 0px 10px")
		self.password_form.setPlaceholderText("USERNAME")
		
		self.login_button = QtWidgets.QPushButton(self)
		self.login_button.setGeometry(QtCore.QRect(320, 360, 200, 50))
		self.login_button.setText("LOGIN")


def window():
	app = QtWidgets.QApplication( sys.argv )
	win = UI_MainWindow()
	win.show()
	sys.exit( app.exec_() )

window()