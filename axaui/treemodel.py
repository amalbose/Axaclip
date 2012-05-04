

from PySide.QtGui import QStandardItemModel
from PySide.QtGui import QStandardItem


class TreeModel(QStandardItemModel):
    
    def __init__(self, parent=None):
        super(TreeModel,self).__init__(parent)
        self._initUI()
    
    def _initUI(self):
        parentItem1 = self.invisibleRootItem()
        for j in range(4):
            item1 = QStandardItem()
            item1.setText("Amal" + str(j))
            for i in range(3):
                insideItem1 = QStandardItem()
                insideItem1.setText("Bose" + str(i))
                item1.appendRow(insideItem1)
            parentItem1.appendRow(item1)