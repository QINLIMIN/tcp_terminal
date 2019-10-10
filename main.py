import sys
from PyQt5 import QtWidgets
import design
import socket
#import gevent

sock = socket.socket()

class gui_example(QtWidgets.QMainWindow, design.Ui_MainWindow):
	
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.openFile.clicked.connect(self.browse_folder)
		self.saveText.clicked.connect(self.save_text)
		self.clearText.clicked.connect(self.clear_text)
		self.btn_tcpConnect.clicked.connect(self.tcp_settings)
		self.actionAbout.triggered.connect(self.info)
		self.actionExit.triggered.connect(self.exit_program)

	def exit_program(self, event):
		reply = QtWidgets.QMessageBox.question(self, 'Exit?', "Close program?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
		
		if reply == QtWidgets.QMessageBox.Yes:
			sys.exit(app.exec_())



	def info(self):
		QtWidgets.QMessageBox.information(self, 'Info', "\"TCP terminal\"\r\nAutor: M. Beletsky\r\nVersion 0.25.1\r\nDemo Version", QtWidgets.QMessageBox.Ok)

	def browse_folder(self):
		self.textBrowser.clear()
		fileName = QtWidgets.QFileDialog.getOpenFileName(self, "Open file", '/home/max')[0]
		print (fileName)
		try:
			file = open(fileName, 'r')
			text = file.read()
			self.textBrowser.append(text)
			file.close()
		except:
			print ("No file")

	def save_text(self):
		fileName = QtWidgets.QFileDialog.getSaveFileName(self, "Save file", '/home/max')[0]
		try:
			file = open(fileName, "w")
			text = self.textBrowser.toPlainText()
			file.write(text)
			file.close()
		except:
			print ("No file")

	def clear_text(self):
		self.textBrowser.clear()

	def start_server(self):
		try:
			port = int(self.txt_port.text())
			sock.bind(('', port))
			sock.listen(1)
			conn, addr = sock.accept()
			print ('connected:', addr)
			
			while True:
				data = conn.recv(1024)
				if not data:
					gevent.slip(0)
					break
				print (data)
		except:
			print ("No!")

	def start_client(self):
		print ("Hi")

	def tcp_settings(self):
		if self.radioServer.isChecked() == True:
			self.start_server()
		if self.radioClient.isChecked() == True:
			self.start_client()


def main():
	app = QtWidgets.QApplication(sys.argv)
	window = gui_example()
	window.show()
	app.exec_()


if __name__ == '__main__':
	main()
