
from PyQt5 import QtWidgets
import sys
from form import Ui_MainWindow


class X(QtWidgets.QMainWindow):
    def __init__(self):
        super(X,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.goster)
    
    def goster(self):
        ad = self.ui.ad.text()
        soyad = self.ui.soyad.text()
        yas = self.ui.yas.text()
        email = self.ui.email.text()

        print('Ad : '+ad)
        print('Soyad : '+soyad)
        print('Yas : '+yas)
        print('Email : '+email)


def start():
    app = QtWidgets.QApplication(sys.argv)
    win = X()

    win.show()

    sys.exit(app.exec_())


start()