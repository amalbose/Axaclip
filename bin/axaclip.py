'''
Created on Apr 22, 2012

@author: amalbose
'''
import sys
from PySide.QtCore import *
from PySide.QtGui import *

class AxaManager(QMainWindow):
    
    def __init__(self,parent=None):
        super(AxaManager,self).__init__(parent)
        self.setGeometry(300,300,600,450)
        self.setWindowTitle("AxaClip - Snippet Manager")

        self.spinner = QLineEdit()
        self.spinner.setText("Howdy!")
        self.spinner.returnPressed.connect(self.UI)
        self.setCentralWidget(self.spinner)

    def UI(self):
        print "pressed" + self.spinner.text()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    axaManagerObj = AxaManager()
    axaManagerObj.show()
    app.exec_()