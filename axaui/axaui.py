'''
Created on May 1, 2012

@author: amalbose
'''

import sys

from PySide.QtGui import QApplication
from PySide.QtGui import QMainWindow
from PySide.QtGui import QWidget
from PySide.QtGui import QHBoxLayout

from axamenubar import AxaMenuBar
from axatexteditor import AxaTextEditor
from axasidebar import AxaSideBar

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
        self._putBody()
        self._centralWidget = None
        
    def _putStatusBar(self):
        "Puts the status bar"
        self.statusBar()
        
    def _putMenuBar(self):
        "Displays the menu bar"
        _menuBar = AxaMenuBar(self)
        self.setMenuBar(_menuBar)
    
    def _putBody(self):
        self._centralWidget = QWidget()
        _hlayout = QHBoxLayout()
        _hlayout.addWidget(self._putSideBar())
        _hlayout.addWidget(self._putTextArea())
        self._centralWidget.setLayout(_hlayout)
        self.setCentralWidget(self._centralWidget)
        
    
    def _putTextArea(self):
        return AxaTextEditor(self._centralWidget)

    def _putSideBar(self):
        return AxaSideBar(self._centralWidget)

    def closeApp(self):
        "Closes the application"
        self.close()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    axaManagerObj = AxaManager()
    axaManagerObj.show()
    sys.exit(app.exec_())
