# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'anapencere.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



# pyuic5 anapencere.ui -o MainWindow.py olusturmak icin yazdil

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AnaPencere(object):
    def setupUi(self, AnaPencere):
        AnaPencere.setObjectName("AnaPencere")
        AnaPencere.resize(740, 458)
        self.centralwidget = QtWidgets.QWidget(AnaPencere)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 100, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 155, 89, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setGeometry(QtCore.QRect(350, 210, 75, 23))
        self.btn.setObjectName("btn")
        self.name_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.name_txt.setGeometry(QtCore.QRect(300, 99, 191, 31))
        self.name_txt.setObjectName("name_txt")
        self.surname_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.surname_txt.setGeometry(QtCore.QRect(300, 150, 191, 31))
        self.surname_txt.setObjectName("surname_txt")
        self.lbl_result = QtWidgets.QLabel(self.centralwidget)
        self.lbl_result.setGeometry(QtCore.QRect(280, 270, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        font.setPointSize(14)
        self.lbl_result.setFont(font)
        self.lbl_result.setObjectName("lbl_result")
        AnaPencere.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AnaPencere)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 740, 21))
        self.menubar.setObjectName("menubar")
        AnaPencere.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AnaPencere)
        self.statusbar.setObjectName("statusbar")
        AnaPencere.setStatusBar(self.statusbar)

        self.retranslateUi(AnaPencere)
        QtCore.QMetaObject.connectSlotsByName(AnaPencere)

    def retranslateUi(self, AnaPencere):
        _translate = QtCore.QCoreApplication.translate
        AnaPencere.setWindowTitle(_translate("AnaPencere", "MainWindow"))
        self.label.setText(_translate("AnaPencere", "Name :"))
        self.label_2.setText(_translate("AnaPencere", "Surname :"))
        self.btn.setText(_translate("AnaPencere", "Bas"))
        self.lbl_result.setText(_translate("AnaPencere", "TextLabel"))
