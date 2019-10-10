import sys
from PyQt5 import QtWidgets
import design



class gui_example(QtWidgets.QMainWindow, design.Ui_MainWindow):
	
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.openFile.clicked.connect(self.browse_folder)
		self.saveText.clicked.connect(self.save_text)
		self.clearText.clicked.connect(self.clear_text)

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



def main():
	app = QtWidgets.QApplication(sys.argv)
	window = gui_example()
	window.show()
	app.exec_()


if __name__ == '__main__':
	main()
