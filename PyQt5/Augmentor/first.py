# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.lblShow = QtWidgets.QLabel(Form)
        self.lblShow.setGeometry(QtCore.QRect(60, 20, 221, 191))
        self.lblShow.setObjectName("lblShow")
        self.btnFIle = QtWidgets.QPushButton(Form)
        self.btnFIle.setGeometry(QtCore.QRect(60, 250, 56, 17))
        self.btnFIle.setObjectName("btnFIle")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lblShow.setText(_translate("Form", "TextLabel"))
        self.btnFIle.setText(_translate("Form", "PushButton"))

