import collections
import pprint

import PySide2
from PySide2.QtCore import Qt
from PySide2.QtGui import QTextCursor
from PySide2.QtWidgets import QPlainTextEdit

from CustomTipWidget import CustomComboBox




class CustomPlainTextEdit(QPlainTextEdit):
    def __init__(self,p):
        super(CustomPlainTextEdit, self).__init__(p)
        self.tipWidget=CustomComboBox(self)
        self.textChanged.connect(self.popupTip)
        self.tipWidget.Autocomplete_Signal.connect(self.autoComplete)
        self.initAttr()
    def initAttr(self):
        self.startListenKey=False
        self.currentEdittingString= ""
        self.cursorPtr =0
        self.stringPtrHead = 0
        self.stringPtrTail = 0
        self.wrapChar={k for k in ["\n",'','\t',' ']}
        self.jumpChar={Qt.Key_Return,Qt.Key_Tab,Qt.Key_Up,Qt.Key_Down}

    def updateListenString(self):
        self.cursorPtr = self.textCursor().position()
        self.currentEdittingString = ""
    def autoComplete(self,res):
        """
        拿到当前的 指针并且插入
        :return:
        """
        selectedString=res["selectedString"]
        key=res["key"]
        if key==Qt.Key_Return:
            self.insertPlainText(selectedString)
        elif key==Qt.Key_Tab:
            tc=self.textCursor()
            tc.select(QTextCursor.SelectionType.WordUnderCursor)
            tc.removeSelectedText()
            self.insertPlainText(selectedString)


    def autoCompleteByChar(self,char):
        """

        :param char:
        :return:
        """
        tc=self.textCursor()
        if char=="{":
            self.insertPlainText("\n\n}")
            tc.movePosition(QTextCursor.Left, n=2)

        self.setTextCursor(tc)



    def popupTip(self):
        """

        :return:
        """

        toText=self.toPlainText()
        self.parent().setStyleSheet(toText)
        if not toText:
            self.stringPtrHead=0
            self.tipWidget.hide()
            return

        inputChar=toText[-1]
        self.autoCompleteByChar(inputChar)
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
                if char in self.wrapChar or not char.isalnum():
                    self.stringPtrHead= len(truncatedHead) - idx
                    break
            for idx,char in enumerate(truncatedTail):
                if not char.isalpha():
                    self.stringPtrTail=len(truncatedTail)+idx
                    break
            # print(self.stringPtrHead,self.cursorPtr)
            self.currentEdittingString= toText[self.stringPtrHead:self.cursorPtr]#truncatedHead#toText[:self.stringPtrTail]#toText[self.stringPtrHead:] +
            print(self.currentEdittingString,self.stringPtrHead,self.cursorPtr)
            self.tipWidget.prefixMatch(self.currentEdittingString)


    def keyPressEvent(self, e:PySide2.QtGui.QKeyEvent) -> None:
        """

        :param e:
        :return:
        """


        if self.tipWidget.isVisible():
            if e.key() not in self.jumpChar:
                super(CustomPlainTextEdit, self).keyPressEvent(e)
        else:
            super(CustomPlainTextEdit, self).keyPressEvent(e)
        self.tipWidget.keyPressEvent(e)
        self.setFocus()


    def focusInEvent(self, e:PySide2.QtGui.QFocusEvent) -> None:
        """

        :param e:
        :return:
        """
        self.updateListenString()


    def focusOutEvent(self, e:PySide2.QtGui.QFocusEvent) -> None:

        self.currentEdittingString = ""
        self.cursorPtr=0


        