# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.openFile = QtWidgets.QPushButton(self.centralwidget)
        self.openFile.setGeometry(QtCore.QRect(10, 20, 100, 31))
        self.openFile.setObjectName("openFile")
        self.saveText = QtWidgets.QPushButton(self.centralwidget)
        self.saveText.setGeometry(QtCore.QRect(10, 70, 100, 31))
        self.saveText.setObjectName("saveText")
        self.textBrowser = QtWidgets.QTextEdit(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(120, 10, 671, 551))
        self.textBrowser.setObjectName("textBrowser")
        self.clearText = QtWidgets.QPushButton(self.centralwidget)
        self.clearText.setGeometry(QtCore.QRect(10, 120, 100, 31))
        self.clearText.setObjectName("clearText")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GUI Example (python)"))
        self.openFile.setText(_translate("MainWindow", "Open File"))
        self.saveText.setText(_translate("MainWindow", "Save Text"))
        self.clearText.setText(_translate("MainWindow", "Clear Text"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

