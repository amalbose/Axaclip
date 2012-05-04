'''
Created on May 3, 2012

@author: amalbose
'''

from PySide.QtGui import QTreeView
#from PySide.QtGui import QAbstractItemView

from treemodel import TreeModel


class AxaSideBar(QTreeView):
    """The menu bar class for AxaClip. Creates and adds various
    menus and their actions.
    """
    def __init__(self, parent=None):
        super(AxaSideBar,self).__init__(parent)
        self._addTree(parent)
    
        
    def _addTree(self,parent):
        self.model = TreeModel()
        self.setModel(self.model)
        #self.setDragDropMode(QAbstractItemView.InternalMove)