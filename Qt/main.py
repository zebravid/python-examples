import sys
import forms
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5 import uic

class ExampleApp(QtWidgets.QMainWindow, forms.Ui_Form):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.browseFun)
    def browseFun(self):
    	self.textEdit.clear()
    	derectory=QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
    	if directory:
        	for filename in os.listdir(directory):
        		textEdit.append(filename)
        	
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ExampleApp()
    ex.show()
    sys.exit(app.exec_())