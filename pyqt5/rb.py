# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rb.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(759, 611)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_ulke = QtWidgets.QLabel(self.centralwidget)
        self.lbl_ulke.setGeometry(QtCore.QRect(100, 230, 161, 51))
        self.lbl_ulke.setText("")
        self.lbl_ulke.setObjectName("lbl_ulke")
        self.lbl_ders = QtWidgets.QLabel(self.centralwidget)
        self.lbl_ders.setGeometry(QtCore.QRect(500, 230, 171, 61))
        self.lbl_ders.setText("")
        self.lbl_ders.setObjectName("lbl_ders")
        self.btn_ulke = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ulke.setGeometry(QtCore.QRect(110, 340, 141, 23))
        self.btn_ulke.setObjectName("btn_ulke")
        self.btn_ders = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ders.setGeometry(QtCore.QRect(520, 330, 141, 23))
        self.btn_ders.setObjectName("btn_ders")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(80, 70, 231, 131))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 20, 160, 88))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.radioABD = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioABD.setObjectName("radioABD")
        self.gridLayout.addWidget(self.radioABD, 2, 0, 1, 1)
        self.radioIng = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioIng.setObjectName("radioIng")
        self.gridLayout.addWidget(self.radioIng, 1, 0, 1, 1)
        self.radioTurkey = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioTurkey.setObjectName("radioTurkey")
        self.gridLayout.addWidget(self.radioTurkey, 0, 0, 1, 1)
        self.radioRusya = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioRusya.setObjectName("radioRusya")
        self.gridLayout.addWidget(self.radioRusya, 3, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(460, 90, 251, 131))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.frame_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(50, 20, 160, 88))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.radioMatematik = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioMatematik.setObjectName("radioMatematik")
        self.gridLayout_2.addWidget(self.radioMatematik, 0, 0, 1, 1)
        self.radioIngilizce = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioIngilizce.setObjectName("radioIngilizce")
        self.gridLayout_2.addWidget(self.radioIngilizce, 3, 0, 1, 1)
        self.radioFizik = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioFizik.setObjectName("radioFizik")
        self.gridLayout_2.addWidget(self.radioFizik, 1, 0, 1, 1)
        self.radioTurkce = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioTurkce.setObjectName("radioTurkce")
        self.gridLayout_2.addWidget(self.radioTurkce, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 759, 21))
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
        self.btn_ulke.setText(_translate("MainWindow", "PushButton"))
        self.btn_ders.setText(_translate("MainWindow", "PushButton"))
        self.radioABD.setText(_translate("MainWindow", "ABD"))
        self.radioIng.setText(_translate("MainWindow", "Ingiltere"))
        self.radioTurkey.setText(_translate("MainWindow", "Turkiye"))
        self.radioRusya.setText(_translate("MainWindow", "Rusya"))
        self.radioMatematik.setText(_translate("MainWindow", "Matematik"))
        self.radioIngilizce.setText(_translate("MainWindow", "Ingilizce"))
        self.radioFizik.setText(_translate("MainWindow", "Fizik"))
        self.radioTurkce.setText(_translate("MainWindow", "Turkce"))
