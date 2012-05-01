'''
Created on May 1, 2012

@author: amalbose
'''

from PySide.QtGui import QMenuBar
from PySide.QtGui import QAction

class AxaMenuBar(QMenuBar):
    def __init__(self, parent=None):
        super(AxaMenuBar,self).__init__(parent)
        
        #creating actions
        
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
        
        _copyAction = QAction("&Copy", parent)
        _editMenu = self.addMenu('&Edit')
        _editMenu.addAction(_copyAction)
        
        #Tools
        
        _toolsMenu = self.addMenu('&Tools')
        
            
    def _addSnippet(self):
        print "Add Snippet"
        
    def _editSnippet(self):
        print "Edit Snippet"