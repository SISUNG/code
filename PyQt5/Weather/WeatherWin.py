# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WeatherWIn.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.Form = QtWidgets.QWidget(MainWindow)
        self.Form.setObjectName("Form")
        self.groupBox = QtWidgets.QGroupBox(self.Form)
        self.groupBox.setGeometry(QtCore.QRect(30, 40, 321, 211))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 41, 9))
        self.label.setObjectName("label")
        self.resultText = QtWidgets.QTextEdit(self.groupBox)
        self.resultText.setGeometry(QtCore.QRect(20, 80, 281, 101))
        self.resultText.setObjectName("resultText")
        self.weatherComboBox = QtWidgets.QComboBox(self.groupBox)
        self.weatherComboBox.setGeometry(QtCore.QRect(60, 30, 211, 16))
        self.weatherComboBox.setObjectName("weatherComboBox")
        self.weatherComboBox.addItem("")
        self.weatherComboBox.addItem("")
        self.weatherComboBox.addItem("")
        self.queryBtn = QtWidgets.QPushButton(self.Form)
        self.queryBtn.setGeometry(QtCore.QRect(70, 320, 56, 17))
        self.queryBtn.setObjectName("queryBtn")
        self.clearBtn = QtWidgets.QPushButton(self.Form)
        self.clearBtn.setGeometry(QtCore.QRect(230, 320, 56, 17))
        self.clearBtn.setObjectName("clearBtn")
        MainWindow.setCentralWidget(self.Form)

        self.retranslateUi(MainWindow)
        self.queryBtn.clicked.connect(MainWindow.queryWeather)
        self.clearBtn.clicked.connect(MainWindow.clearResult)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "查询城市天气"))
        self.label.setText(_translate("MainWindow", "城市"))
        self.weatherComboBox.setItemText(0, _translate("MainWindow", "北京"))
        self.weatherComboBox.setItemText(1, _translate("MainWindow", "天津"))
        self.weatherComboBox.setItemText(2, _translate("MainWindow", "上海"))
        self.queryBtn.setText(_translate("MainWindow", "查询"))
        self.clearBtn.setText(_translate("MainWindow", "清空"))

