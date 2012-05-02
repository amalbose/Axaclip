'''
Created on May 1, 2012

@author: amalbose
'''

from PySide.QtGui import QMenuBar
from PySide.QtGui import QAction

class AxaMenuBar(QMenuBar):
    """The menu bar class for AxaClip. Creates and adds various
    menus and their actions.
    """
    def __init__(self, parent=None):
        super(AxaMenuBar,self).__init__(parent)
        self._initUI(parent)
        
    def _initUI(self,parent):
        "Adds the menu items into the menu bar"
        #File Menu
        #add action
        _addAction = QAction("Add Snippet", parent)
        _addAction.setShortcut("Ctrl+N")
        _addAction.setStatusTip('Add new Snippet')
        _addAction.triggered.connect(self._addSnippet)
        
        #edit action
        _editAction = QAction("Edit Snippet", parent)
        _editAction.setShortcut("Ctrl+O")
        _editAction.setStatusTip('Edit Snippet')
        _editAction.triggered.connect(self._editSnippet)
        
        #exit action
        _exitAction = QAction("&Exit", parent)
        _exitAction.setShortcut("Ctrl+Q")
        _exitAction.setStatusTip('Exit application')
        _exitAction.triggered.connect(parent.closeApp)
        
        # Adding to file menu
        _fileMenu = self.addMenu('&File')
        _fileMenu.addAction(_addAction)
        _fileMenu.addAction(_editAction)
        _fileMenu.addSeparator()
        _fileMenu.addAction(_exitAction)
        
        #Edit Menu
        #copy action
        _copyAction = QAction("&Copy", parent)
        _copyAction.setShortcut("Ctrl+C")
        _copyAction.setStatusTip('Copy text')
        
        _editMenu = self.addMenu('&Edit')
        _editMenu.addAction(_copyAction)
        
        #Tools
        
        _toolsMenu = self.addMenu('&Tools')
        
            
    def _addSnippet(self):
        print "Add Snippet"
        
    def _editSnippet(self):
        print "Edit Snippet"