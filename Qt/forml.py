# -*- coding: utf-8 -*-# Form implementation generated from reading ui file 'forml.ui'## Created: Wed Apr 10 14:22:00 2019#      by: PyQt5 UI code generator 5.3.2## WARNING! All changes made in this file will be lost!from PyQt5 import QtCore, QtGui, QtWidgetsclass Ui_Form(object):    def setupUi(self, Form):        Form.setObjectName("Form")        Form.resize(400, 300)        self.table=QtWidgets.QTableWidget(Form)        self.table.setGeometry(QtCore.QRect(130, 220,450, 271))        self.table.setRowCount(5)        self.table.setColumnCount(5)        self.table.setObjectName("textEdit")        self.lineEdit = QtWidgets.QLineEdit(Form)        self.lineEdit.setGeometry(QtCore.QRect(130, 20, 113, 20))        self.lineEdit.setObjectName("lineEdit")        self.lineEdit_2 = QtWidgets.QLineEdit(Form)        self.lineEdit_2.setGeometry(QtCore.QRect(130, 110, 113, 20))        self.lineEdit_2.setObjectName("lineEdit_2")        self.lineEdit_3 = QtWidgets.QLineEdit(Form)        self.lineEdit_3.setGeometry(QtCore.QRect(130, 80, 113, 20))        self.lineEdit_3.setObjectName("lineEdit_3")        self.lineEdit_4 = QtWidgets.QLineEdit(Form)        self.lineEdit_4.setGeometry(QtCore.QRect(130, 50, 113, 20))        self.lineEdit_4.setObjectName("lineEdit_,4")                self.lineEdit_5= QtWidgets.QLineEdit(Form)        self.lineEdit_5.setGeometry(QtCore.QRect(130, 140, 113, 20))        self.lineEdit_5.setObjectName("lineEdit_5")        self.pushButton = QtWidgets.QPushButton(Form)        self.pushButton.setGeometry(QtCore.QRect(30, 20, 75, 23))        self.pushButton.setObjectName("pushButton")        self.pushButton_2 = QtWidgets.QPushButton(Form)        self.pushButton_2.setGeometry(QtCore.QRect(30, 50, 75, 23))        self.pushButton_2.setObjectName("pushButton_2")        self.pushButton_3 = QtWidgets.QPushButton(Form)        self.pushButton_3.setGeometry(QtCore.QRect(30, 80, 75, 23))        self.pushButton_3.setObjectName("pushButton_3")        self.pushButton_4 = QtWidgets.QPushButton(Form)        self.pushButton_4.setGeometry(QtCore.QRect(30, 110, 75, 23))        self.pushButton_4.setObjectName("pushButton_4")        self.pushButton_5 = QtWidgets.QPushButton(Form)        self.pushButton_5.setGeometry(QtCore.QRect(30, 140, 75, 23))        self.pushButton_5.setObjectName("pushButton_5")        self.pushButton_6 = QtWidgets.QPushButton(Form)        self.pushButton_6.setGeometry(QtCore.QRect(30, 170, 75, 23))        self.pushButton_6.setObjectName("pushButton_6")        self.retranslateUi(Form)        QtCore.QMetaObject.connectSlotsByName(Form)    def retranslateUi(self, Form):        _translate = QtCore.QCoreApplication.translate        Form.setWindowTitle(_translate("Form", "Form"))        self.pushButton.setText(_translate("Form", "Brow"))        self.pushButton_2.setText(_translate("Form", "Insert"))        self.pushButton_3.setText(_translate("Form", "removeRow"))        self.pushButton_4.setText(_translate("Form", "ConvertE"))        self.pushButton_5.setText(_translate("Form", "PushButton"))        self.pushButton_6.setText(_translate("Form", "EditUpdate"))        self.lineEdit.setText(_translate("Form","insert"))