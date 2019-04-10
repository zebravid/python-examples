import sys
import forms
from backOp import Book
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5 import uic

class ExampleApp(QtWidgets.QMainWindow, forms.Ui_Form):
    def __init__(self,db):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)
        self.db=db
        for element in self.db.view():
        	for input in element:
        		self.textEdit.append(str(input))
        self.pushButton.clicked.connect(self.browseFun)
    def browseFun(self):
    	
    	self.textEdit.clear()
    	self.textEdit.append("77777")
    	derectory=QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
    	
    	if derectory:
    		
        	for filename in os.listdir(derectory):
        		self.textEdit.append(filename)
        		#adding items to the db
        		self.db.insert(filename,"","","")
        	
        		
   	

if __name__ == '__main__':
	bookDb=Book("book.db")
	app = QApplication(sys.argv)
	ex = ExampleApp(bookDb)
	ex.show()
	sys.exit(app.exec_())