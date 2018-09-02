# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'views/ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

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
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnrefresh.setText(_translate("MainWindow", "Refresh"))
        self.btnnewmsg.setText(_translate("MainWindow", "New Message"))
        self.maintab.setTabText(self.maintab.indexOf(self.tab_sms), _translate("MainWindow", "SMS"))
        self.chkdata.setText(_translate("MainWindow", "Data"))
        self.chkwifi.setText(_translate("MainWindow", "Wifi"))
        self.maintab.setTabText(self.maintab.indexOf(self.tab_config), _translate("MainWindow", "Config"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

