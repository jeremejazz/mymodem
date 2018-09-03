# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'views/ui/mainwindow.ui',
# licensing of 'views/ui/mainwindow.ui' applies.
#
# Created: Mon Sep  3 12:33:54 2018
#      by: pyside2-uic  running on PySide2 5.11.1a1.dev1535107939337
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(484, 487)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.maintab = QtWidgets.QTabWidget(self.centralwidget)
        self.maintab.setObjectName("maintab")
        self.tab_sms = QtWidgets.QWidget()
        self.tab_sms.setObjectName("tab_sms")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_sms)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 5, 1, 1)
        self.btnrefresh = QtWidgets.QPushButton(self.tab_sms)
        self.btnrefresh.setObjectName("btnrefresh")
        self.gridLayout.addWidget(self.btnrefresh, 0, 6, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.tab_sms)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 1, 1, 1, 6)
        self.btnnewmsg = QtWidgets.QPushButton(self.tab_sms)
        self.btnnewmsg.setObjectName("btnnewmsg")
        self.gridLayout.addWidget(self.btnnewmsg, 0, 1, 1, 3)
        self.maintab.addTab(self.tab_sms, "")
        self.tab_config = QtWidgets.QWidget()
        self.tab_config.setObjectName("tab_config")
        self.formLayout = QtWidgets.QFormLayout(self.tab_config)
        self.formLayout.setObjectName("formLayout")
        self.chkdata = QtWidgets.QCheckBox(self.tab_config)
        self.chkdata.setObjectName("chkdata")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.chkdata)
        self.chkwifi = QtWidgets.QCheckBox(self.tab_config)
        self.chkwifi.setObjectName("chkwifi")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.chkwifi)
        self.maintab.addTab(self.tab_config, "")
        self.horizontalLayout.addWidget(self.maintab)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 484, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.maintab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.btnrefresh.setText(QtWidgets.QApplication.translate("MainWindow", "Refresh", None, -1))
        self.btnnewmsg.setText(QtWidgets.QApplication.translate("MainWindow", "New Message", None, -1))
        self.maintab.setTabText(self.maintab.indexOf(self.tab_sms), QtWidgets.QApplication.translate("MainWindow", "SMS", None, -1))
        self.chkdata.setText(QtWidgets.QApplication.translate("MainWindow", "Data", None, -1))
        self.chkwifi.setText(QtWidgets.QApplication.translate("MainWindow", "Wifi", None, -1))
        self.maintab.setTabText(self.maintab.indexOf(self.tab_config), QtWidgets.QApplication.translate("MainWindow", "Config", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

