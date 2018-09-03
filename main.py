#!/usr/bin/env python3


from PySide2.QtWidgets import QApplication, QMainWindow
from views.compiled.mainwindow import Ui_MainWindow
from mymodem import MyModem

import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
 
    mymodem = MyModem()
     
    mymodem.show()
    sys.exit(app.exec_())
