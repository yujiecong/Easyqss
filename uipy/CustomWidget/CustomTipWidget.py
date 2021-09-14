import json
import pprint

import PySide2
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from CustomTipWidget_Ui import Ui_TipWidget


class CustomComboBox(QWidget, Ui_TipWidget):
    Autocomplete_Signal = Signal(dict)

    def __init__(self, p):
        super(CustomComboBox, self).__init__(p)
        self.setupUi(self)
        # self.setFixedSize(100, 50)
        self.initAttr()
        self.hide()
        self.initQSSAttr()
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
        self.topItem = None
        self.setFocusPolicy(Qt.NoFocus)
        self.setAttribute(Qt.WA_ShowWithoutActivating, True)
        # self.setWindowFlag(Qt.WindowStaysOnTopHint)

    def initQSSAttr(self):
        """

        :return:
        """

        # self.keywords = {"css":[
        #     'background',
        #     'background-attachment',
        #     'background-color',
        #     'background-image',
        #     'background-position',
        #     'background-repeat',
        #     'background-clip',
        #     'background-origin',
        #     'background-size',
        #     'border',
        #     'border-bottom',
        #     'border-bottom-color',
        #     'border-bottom-style',
        #     'border-bottom-width',
        #     'border-color',
        #     'border-left',
        #     'border-left-color',
        #     'border-left-style',
        #     'border-left-width',
        #     'border-right',
        #     'border-right-color',
        #     'border-right-style',
        #     'border-right-width',
        #     'border-style',
        #     'border-top',
        #     'border-top-color',
        #     'border-top-style',
        #     'border-top-width',
        #     'border-width',
        #     'outline',
        #     'outline-color',
        #     'outline-style',
        #     'outline-width',
        #     'border-bottom-left-radius',
        #     'border-bottom-right-radius',
        #     'border-image',
        #     'border-image-outset',
        #     'border-image-repeat',
        #     'border-image-slice',
        #     'border-image-source',
        #     'border-image-width',
        #     'border-radius',
        #     'border-top-left-radius',
        #     'border-top-right-radius',
        #     'box-decoration-break',
        #     'box-shadow',
        #     'overflow-x',
        #     'overflow-y',
        #     'overflow-style',
        #     'rotation',
        #     'rotation-point',
        #     'bottom',
        #     'clear',
        #     'clip',
        #     'cursor',
        #     'display',
        #     'float',
        #     'left',
        #     'overflow',
        #     'position',
        #     'right',
        #     'top',
        #     'vertical-align',
        #     'visibility',
        #     'z-index',
        #     'color-profile',
        #     'opacity',
        #     'rendering-intent',
        #     'color',
        #     'direction',
        #     'letter-spacing',
        #     'line-height',
        #     'text-align',
        #     'text-decoration',
        #     'text-indent',
        #     'text-shadow',
        #     'text-transform',
        #     'unicode-bidi',
        #     'white-space',
        #     'word-spacing',
        #     'hanging-punctuation',
        #     'punctuation-trim',
        #     'text-align-last',
        #     'text-emphasis',
        #     'text-justify',
        #     'text-outline',
        #     'text-overflow',
        #     'text-shadow',
        #     'text-wrap',
        #     'word-break',
        #     'word-wrap',
        #     'height',
        #     'max-height',
        #     'max-width',
        #     'min-height',
        #     'min-width',
        #     'width',
        #     'font',
        #     'font-family',
        #     'font-size',
        #     'font-size-adjust',
        #     'font-stretch',
        #     'font-style',
        #     'font-variant',
        #     'font-weight',
        #     'margin',
        #     'margin-bottom',
        #     'margin-left',
        #     'margin-right',
        #     'margin-top',
        #     'padding',
        #     'padding-bottom',
        #     'padding-left',
        #     'padding-right',
        #     'padding-top']}

        # with open("data/cssKeyword.json","w") as f:
        #     json.dump(self.keywords,f,sort_keys=True,indent=4,
        #               separators=(
        #                   ',',
        #                   ': '))
        with open("data/cssKeyword.json","r") as f:
            self.keywords=json.load(f)

        for cssKeyword in self.keywords["css"]:
            self.listWidget.addItem(cssKeyword)

    def initItems(self):
        for key in list(globals().keys()):
            if key.startswith("Q"):
                self.listWidget.addItem(key)

        self.listWidget.sortItems(Qt.SortOrder.AscendingOrder)

    def prefixMatch(self, prefix: str):
        """

        :param prefix:
        :return:
        """
        if prefix.isalnum():
            self.prefix = prefix.lower()
            topItem = None
            for childIdx in range(self.listWidget.count() - 1, -1, -1):
                it = self.listWidget.item(childIdx)
                if it.text().lower().startswith(self.prefix):
                    # it.setHidden(False)
                    topItem = it
                    topItem.setSelected(True)
                    row=self.listWidget.row(topItem)
                    self.listWidget.verticalScrollBar().setValue(row)
                # else:
                #     it.setHidden(True)
            if topItem:
                self.listWidget.setItemSelected(topItem, True)
                self.topItem = topItem
                self.show()


    def selectByHand(self, *args):
        """

        :return:
        """
        item = self.listWidget.selectedItems()[0]

        res={
            "selectedString":item.text()[len(self.prefix):],
            "key":-1
        }
        self.Autocomplete_Signal.emit(res)
        self.hide()

    def keyPressEvent(self, event):
        """

        :param event:
        :return:
        """

        if self.isVisible():
            # scrollRows=self.listWidget.verticalScrollBar().height()
            # print(self.listWidget.verticalScrollBar().value())
            if event.key() == Qt.Key_Down:
                idx = self.listWidget.indexFromItem(self.topItem)
                nextRow = idx.row() + 1
                nextItem = self.listWidget.item(nextRow)
                while nextItem.isHidden():
                    nextRow = idx.row() + 1
                    nextItem = self.listWidget.item(nextRow)

                self.listWidget.setItemSelected(nextItem, True)
                self.topItem = nextItem

                # scrollBarHeight=self.listWidget.verticalScrollBar().height()

                self.listWidget.verticalScrollBar().setValue(nextRow-5)
            elif event.key() == Qt.Key_Up:
                idx = self.listWidget.indexFromItem(self.topItem)

                if idx.row() > 0:
                    nextRow = idx.row() - 1
                    nextItem = self.listWidget.item(nextRow)
                    while nextItem.isHidden() and nextRow>0:
                        idx = self.listWidget.indexFromItem(nextItem)
                        nextRow = idx.row() - 1
                        nextItem = self.listWidget.item(nextRow)

                    self.listWidget.setItemSelected(nextItem, True)
                    self.topItem = nextItem
                    # if nextRow>5:
                    self.listWidget.verticalScrollBar().setValue(nextRow-5)
                    # else:
                    #     self.listWidget.verticalScrollBar().setValue(nextRow )
            elif event.key() == Qt.Key_Return:
                if self.topItem:
                    res = {
                        "selectedString": self.topItem.text()[len(self.prefix):],
                        "key": Qt.Key_Return
                    }
                    self.Autocomplete_Signal.emit(res)
                    self.hide()
            elif event.key() == Qt.Key_Tab:
                if self.topItem:
                    res = {
                        "selectedString": self.topItem.text(),
                        "key": Qt.Key_Tab
                    }
                    self.Autocomplete_Signal.emit(
                        res)
                    self.hide()
        super(CustomComboBox, self).keyPressEvent(event)

    def showEvent(self, event: PySide2.QtGui.QShowEvent) -> None:

        super(CustomComboBox, self).showEvent(event)
