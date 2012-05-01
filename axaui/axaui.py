'''
Created on May 1, 2012

@author: amalbose
'''

import sys

from PySide.QtGui import QApplication
from PySide.QtGui import QMainWindow

from axamenubar import AxaMenuBar


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
APPLICATION_NAME = "AxaClip - Snippet Manager"

class AxaManager(QMainWindow):

    
    def __init__(self, parent=None):
        super(AxaManager, self).__init__(parent)
        self.resize(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.setWindowTitle(APPLICATION_NAME)
        self._putStatusBar()
        self._putMenuBar()
        
    def _putStatusBar(self):
        self.statusBar()
        
    def _putMenuBar(self):
        _menuBar = AxaMenuBar(self)
        self.setMenuBar(_menuBar)
        
    def closeApp(self):
        self.close()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    axaManagerObj = AxaManager()
    axaManagerObj.show()
    sys.exit(app.exec_())
