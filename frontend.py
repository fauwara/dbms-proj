from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class myWindow( QMainWindow ):
	def __init__(self):
		super( myWindow,self ).__init__()
		
		self.setGeometry( 100, 100, 500, 500 ) # x, y, width, height
		self.setWindowTitle( "DISTRIBUTOR 101" )

		self.initUI()

	def initUI(self):
		self.label = QtWidgets.QLabel( self )
		self.label.setText( "DISTRIBUTOR 101" )
		self.label.move( 50,50 )
		
		self.guestLogin = QtWidgets.QPushButton( self )
		self.guestLogin.setText( "GUEST" )
		self.guestLogin.move( 50, 100 )
		self.guestLogin.setCheckable(True)
		self.guestLogin.clicked.connect(self.printHello)

	# some functions when you click buttons
	def printHello(self):
		print('hello')


def window():
	app = QApplication( sys.argv )
	win = myWindow()
	win.show()
	sys.exit( app.exec_() )

window()