# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EasyqssMain_Ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtWidgets import *

from uipy.CustomWidget.CustomPlainTextEdit import CustomPlainTextEdit


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(932, 581)
        MainWindow.setStyleSheet(u"background-color: rgb(30, 30, 30);\n"
"font: 75 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"\n"
"color: rgb(191, 191, 191);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.plainTextEdit = CustomPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.horizontalLayout.addWidget(self.plainTextEdit)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 932, 25))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menuxuanze = QMenu(self.menubar)
        self.menuxuanze.setObjectName(u"menuxuanze")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menuxuanze.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91", None))
        self.menuxuanze.setTitle(QCoreApplication.translate("MainWindow", u"\u9009\u62e9", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u4e3b\u9898", None))
    # retranslateUi

