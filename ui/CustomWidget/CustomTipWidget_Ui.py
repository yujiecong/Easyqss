# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CustomTipWidget_Ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_TipWidget(object):
    def setupUi(self, TipWidget):
        if not TipWidget.objectName():
            TipWidget.setObjectName(u"TipWidget")
        TipWidget.resize(394, 183)
        self.horizontalLayout = QHBoxLayout(TipWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.listWidget = QListWidget(TipWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout.addWidget(self.listWidget)


        self.retranslateUi(TipWidget)

        QMetaObject.connectSlotsByName(TipWidget)
    # setupUi

    def retranslateUi(self, TipWidget):
        TipWidget.setWindowTitle(QCoreApplication.translate("TipWidget", u"Form", None))
    # retranslateUi

