# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cb.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(753, 579)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setGeometry(QtCore.QRect(210, 240, 75, 23))
        self.btn.setObjectName("btn")
        self.lbl = QtWidgets.QLabel(self.centralwidget)
        self.lbl.setGeometry(QtCore.QRect(430, 100, 201, 101))
        self.lbl.setText("")
        self.lbl.setObjectName("lbl")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(150, 50, 181, 171))
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 50, 72, 65))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cb_spor = QtWidgets.QCheckBox(self.layoutWidget)
        self.cb_spor.setObjectName("cb_spor")
        self.verticalLayout.addWidget(self.cb_spor)
        self.db_muzik = QtWidgets.QCheckBox(self.layoutWidget)
        self.db_muzik.setObjectName("db_muzik")
        self.verticalLayout.addWidget(self.db_muzik)
        self.cb_dans = QtWidgets.QCheckBox(self.layoutWidget)
        self.cb_dans.setObjectName("cb_dans")
        self.verticalLayout.addWidget(self.cb_dans)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 753, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn.setText(_translate("MainWindow", "Tikla"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.cb_spor.setText(_translate("MainWindow", "spor"))
        self.db_muzik.setText(_translate("MainWindow", "muzik"))
        self.cb_dans.setText(_translate("MainWindow", "dans"))