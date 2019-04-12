#pylint:disable=E0001
import sys
import forml
from backOp import Book
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5 import uic

class ExampleApp(QtWidgets.QMainWindow, forml.Ui_Form):
    def __init__(self,db):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)
        self.db=db
        for element in self.db.view():
        	for input in element:
        		self.listView.addItem(str(input))
        #connection for buttons and user interactions
        #sends text in selected item to show in lineEdit_4
        self.listView.itemSelectionChanged.connect(self.itemAct)
        self.pushButton.clicked.connect(self.browseFun)
        self.pushButton_2.clicked.connect(self.addTextodb)
        
        self.listView.addItem(str("uĝgggggggt"))
    #adds text from selected item in listWidget
    def itemAct(self):
    	myi=self.listView.currentItem()
    	self.lineEdit_4.setText(myi.text())
    	#pass
    	
    def browseFun(self):
    	
    	#self.listVew.clear()
    	self.listView.addItem("77777")
    	derectory=QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
    	
    	if derectory:
    		
        	for filename in os.listdir(derectory):
        		self.listView.addItem(filename)
        		#adding items to the db
        		self.db.insert(filename,"","","")
    def addTextodb(self):
    	
    	textVal=self.lineEdit.text()+"*****"
    	#myItem=QtWidgets.QListWidgetItem("&&&&&&")
    	self.db.insert(textVal,"","","")
    	self.listView.addItem(textVal)
      	
        		
        		
   	

if __name__ == '__main__':
	bookDb=Book("bookek.db")
	app = QApplication(sys.argv)
	ex = ExampleApp(bookDb)
	ex.show()
	sys.exit(app.exec_())