import collections
import pprint

import PySide2
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QPlainTextEdit

from CustomTipWidget import CustomComboBox




class CustomPlainTextEdit(QPlainTextEdit):
    def __init__(self,p):
        super(CustomPlainTextEdit, self).__init__(p)
        self.tipWidget=CustomComboBox(self)
        self.cursorPositionChanged.connect(self.popupTip)
        self.tipWidget.Autocomplete_Signal.connect(self.autoComplete)
        self.initAttr()
    def initAttr(self):
        self.startListenKey=False
        self.currentEdittingString= ""
        self.cursorPtr =0
        self.stringPtrHead = 0
        self.stringPtrTail = 0
        self.wrapChar={k:k for k in ["\n",'','\t']}

    def updateListenString(self):
        self.cursorPtr = self.textCursor().position()
        self.currentEdittingString = ""
    def autoComplete(self,completedString):
        """
        拿到当前的 指针并且插入
        :return:
        """
        self.insertPlainText(completedString)



    def popupTip(self):
        """

        :return:
        """
        toText=self.toPlainText()
        if not toText:
            return

        inputChar=toText[-1]
        self.cursorPtr = self.textCursor().position()
        if inputChar in self.wrapChar:
            self.tipWidget.hide()

        else:
            cr=self.cursorRect()
            cursorX, cursorY, cursorWidth, cursorHeight=cr.x(),cr.y(),cr.width(),cr.height()
            self.tipWidget.move(cursorX, cursorY + cursorHeight)

            truncatedTail= toText[self.cursorPtr:]
            truncatedHead = toText[:self.cursorPtr+1]
            for idx,char in enumerate(truncatedHead[::-1]):
                if char in self.wrapChar:
                    self.stringPtrHead= len(truncatedHead) - idx
                    break
            for idx,char in enumerate(truncatedTail):
                if not char.isalpha():
                    self.stringPtrTail=len(truncatedTail)+idx
                    break
            print(self.stringPtrHead,self.cursorPtr)
            self.currentEdittingString= toText[self.stringPtrHead:self.cursorPtr]#truncatedHead#toText[:self.stringPtrTail]#toText[self.stringPtrHead:] +
            self.tipWidget.prefixMatch(self.currentEdittingString)

            print(self.currentEdittingString)




    def keyPressEvent(self, e:PySide2.QtGui.QKeyEvent) -> None:
        """

        :param e:
        :return:
        """


        if self.tipWidget.isVisible():
            if e.key() != Qt.Key_Return:
                super(CustomPlainTextEdit, self).keyPressEvent(e)
            else:
                pass
        else:
            super(CustomPlainTextEdit, self).keyPressEvent(e)
        self.tipWidget.keyPressEvent(e)
    def focusInEvent(self, e:PySide2.QtGui.QFocusEvent) -> None:
        """

        :param e:
        :return:
        """
        self.updateListenString()


    def focusOutEvent(self, e:PySide2.QtGui.QFocusEvent) -> None:

        self.currentEdittingString = ""
        self.cursorPtr=0


        