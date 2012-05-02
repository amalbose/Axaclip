'''
Created on May 1, 2012

@author: amalbose
'''

import sys

from PySide.QtGui import QApplication
from PySide.QtGui import QMainWindow

from axamenubar import AxaMenuBar

#Width of the window
WINDOW_WIDTH = 800

#height of the window
WINDOW_HEIGHT = 600

#Application Title
APPLICATION_TITLE = "AxaClip - Snippet Manager"

class AxaManager(QMainWindow):
    """
    The GUI Window for Axaclip application.
    """
    
    def __init__(self, parent=None):
        "Initializes MainWindow and displays contents"
        super(AxaManager, self).__init__(parent)
        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setWindowTitle(APPLICATION_TITLE)
        self._putStatusBar()
        self._putMenuBar()
        
    def _putStatusBar(self):
        "Puts the status bar"
        self.statusBar()
        
    def _putMenuBar(self):
        "Displays the menu bar"
        _menuBar = AxaMenuBar(self)
        self.setMenuBar(_menuBar)
        
    def closeApp(self):
        "Closes the application"
        self.close()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    axaManagerObj = AxaManager()
    axaManagerObj.show()
    sys.exit(app.exec_())
