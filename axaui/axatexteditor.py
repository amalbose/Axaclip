'''
Created on May 2, 2012

@author: amalbose
'''

from PySide.QtGui import QTextEdit

class AxaTextEditor(QTextEdit):
    """The menu bar class for AxaClip. Creates and adds various
    menus and their actions.
    """
    def __init__(self, parent=None):
        super(AxaTextEditor,self).__init__(parent)