import PySide2
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from CustomTipWidget_Ui import Ui_TipWidget


class CustomComboBox(QWidget,Ui_TipWidget):
    Autocomplete_Signal=Signal(str)
    def __init__(self,p):
        super(CustomComboBox, self).__init__(p)
        self.setupUi(self)
        # self.setFixedSize(100, 50)
        self.initAttr()
        self.hide()
        self.initItems()

        self.initConnection()
    def initConnection(self):
        """

        :return:
        """
        self.listWidget.itemClicked.connect(self.selectByHand)
    def initAttr(self):
        """

        :return:
        """
        self.topItem=None
        self.setFocusPolicy(Qt.NoFocus)
        self.setAttribute(Qt.WA_ShowWithoutActivating,True)
        # self.setWindowFlag(Qt.WindowStaysOnTopHint)
    def initItems(self):
        for key in list(globals().keys()):
            if key.startswith("Q"):
                self.listWidget.addItem(key)

    def prefixMatch(self,prefix:str):
        """

        :param prefix:
        :return:
        """
        self.prefix=prefix.lower()
        topItem=None
        for childIdx in range(self.listWidget.count()-1,-1,-1):
            it=self.listWidget.item(childIdx)
            it:QListWidgetItem
            if it.text().lower().startswith(self.prefix):
                it.setHidden(False)
                topItem=it
            else:
                it.setHidden(True)
        if topItem:
            self.listWidget.setItemSelected(topItem, True)
            self.topItem=topItem
            self.show()



    def selectByHand(self,*args):
        """

        :return:
        """
        item=self.listWidget.selectedItems()[0]
        self.Autocomplete_Signal.emit(item.text()[len(self.prefix):])
        self.hide()
    def keyPressEvent(self, event):
        """

        :param event:
        :return:
        """

        if self.isVisible():
            if event.key()==Qt.Key_Down:
                idx=self.listWidget.indexFromItem(self.topItem)
                nextRow=idx.row()+1
                nextItem=self.listWidget.item(nextRow)
                self.listWidget.setItemSelected(nextItem,True)
                self.topItem=nextItem
                self.listWidget.verticalScrollBar().setValue(nextRow)
            elif event.key()==Qt.Key_Up:
                idx=self.listWidget.indexFromItem(self.topItem)
                if idx.row()>0:
                    nextRow=idx.row()-1
                    nextItem=self.listWidget.item(nextRow)
                    self.listWidget.setItemSelected(nextItem,True)
                    self.topItem=nextItem
                    self.listWidget.verticalScrollBar().setValue(nextRow)
            elif event.key()==Qt.Key_Return:
                if self.topItem :
                    self.Autocomplete_Signal.emit(self.topItem.text()[len(self.prefix):])
                    self.hide()
        super(CustomComboBox, self).keyPressEvent(event)

    def showEvent(self, event:PySide2.QtGui.QShowEvent) -> None:

        super(CustomComboBox, self).showEvent(event)



