#pylint:disable=E0001
import sys
import sip
import forml
from backOp import Book
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5 import uic

class ExampleApp(QtWidgets.QMainWindow, forml.Ui_Form):
    def __init__(self,db):
        super(ExampleApp,self).__init__()
        self.setupUi(self)
        self.db=db
        self.model=self.table.model()
        
        #let user select rows
        self.table.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        
        #prevent user to edit table data not from interface
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        
        self.table.setRowCount(0)
        #call to backOp function to list all rows
        result=self.db.view()
        #fill the whole tabnle
        for row_n,row_d in enumerate(result):
        	self.table.insertRow(row_n)
        	for col_n,input in enumerate(row_d):
        		self.table.setItem(row_n,col_n,QtWidgets.QTableWidgetItem(str(input)))
        		
        #connection for buttons and user interaction
        #fills edit fields with data from a row
        #TODO update values and rewrite selected row
        self.table.clicked.connect(self.itemAct)
        #opens browsing window
        self.pushButton.clicked.connect(self.browseFun)
        #adds fields to database
        self.pushButton_2.clicked.connect(self.addTextodb)
        #removes selected row from table and database
        self.pushButton_3.clicked.connect(self.removeTextodb)
       
    
    #adds text from selected item in listWidget
    
    def removeTextodb(self):
    	r=self.table.currentRow()
    	index=self.model.index(r,0)
    	idNum=self.model.data(index)
    	self.lineEdit.setText(idNum)
    	self.db.delete(idNum)
    	self.table.removeRow(r)
    	
    def itemAct(self):
    	r=self.table.currentRow()
    	if r :
    		myi=self.table.item(r,0).text()
    		self.lineEdit.setText(myi)
    		
    		myi1=self.table.item(r,1).text()
    		self.lineEdit_2.setText(myi1)
    		
    		myi2=self.table.item(r,2).text()
    		self.lineEdit_3.setText(myi2)
    		myi3=self.table.item(r,3).text()
    		self.lineEdit_4.setText(myi3)
    		
    	else:
    		self.lineEdit_4.setText("select the row")
   #TODO find an useful implimentation for file browser
   #maybe for backup and csv conversion	
    def browseFun(self):
    	derectory=QtWidgets.QFileDialog.getExistingDirectory(self, "676655")
    	
    	if derectory:
    		
        	for filename in os.listdir(derectory):
        		self.table.addItem(filename)
        		#adding items to the db
        	#	self.db.insert(filename,"","","")
        		
    def addTextodb(self):
    	
    	#get the id from database using maxId()
    	
    	textVal=self.lineEdit.text()
    	textVal1=self.lineEdit_2.text()
    	textVal2=self.lineEdit_3.text()
    	textVal3=self.lineEdit_4.text()
    	r=self.table.rowCount()
    	self.db.insert(textVal,textVal1,textVal2,textVal3)
    	myId=self.db.maxId()
    	it0=QtWidgets.QTableWidgetItem(str(myId))
    	it1=QtWidgets.QTableWidgetItem(textVal)
    	it2=QtWidgets.QTableWidgetItem(textVal1)
    	it3=QtWidgets.QTableWidgetItem(textVal2)
    	it4=QtWidgets.QTableWidgetItem(textVal3)
    	
    	self.table.insertRow(r)
    	self.table.setItem(r,0,it0)
    	self.table.setItem(r,1,it1)
    	self.table.setItem(r,2,it2)
    	self.table.setItem(r,3,it3)
    	self.table.setItem(r,4,it4)
      	
        		
        		
   	

if __name__ == '__main__':
	bookDb=Book("bo.db")
	app = QApplication(sys.argv)
	ex = ExampleApp(bookDb)
	ex.show()
	sys.exit(app.exec_())
