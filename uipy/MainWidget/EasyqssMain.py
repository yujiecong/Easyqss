import sys

import PySide2
from PySide2.QtWidgets import QMainWindow, QApplication

from ui.MainWidget.EasyqssMain_Ui import Ui_MainWindow

class Easyqss(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Easyqss, self).__init__()
        self.setupUi(self)
    def mousePressEvent(self, e:PySide2.QtGui.QMouseEvent) -> None:
        self.setFocus()
        super(Easyqss, self).mousePressEvent(e)

if __name__ == '__main__':
    app=QApplication()
    Eq=Easyqss()
    Eq.show()
    sys.exit(app.exec_())
