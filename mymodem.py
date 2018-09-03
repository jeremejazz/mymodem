#!/usr/bin/env python3

# Extend generated template here
from PySide2.QtWidgets import QApplication, QMainWindow, QDesktopWidget
from views.compiled.mainwindow import Ui_MainWindow

import sys

class MyModem(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyModem, self).__init__()

        self.setupUi(self)
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())