from PyQt5 import QtWidgets
import sys
from MainWindow import Ui_AnaPencere

class App(QtWidgets.QMainWindow): # aslinda yeni bir pencere olusturoyruz fakan icini burda doldurmuyoruz

    def __init__(self):
        super(App,self).__init__()

        self.ui = Ui_AnaPencere()
        self.ui.setupUi(self)
        self.ui.btn.clicked.connect(self.goster)

    def goster(self):

        name = self.ui.name_txt.text()
        surname = self.ui.surname_txt.text()

        self.ui.lbl_result.setText('Name : '+name+" Surname : "+surname)



def exeapp():
    app = QtWidgets.QApplication(sys.argv)

    win = App()

    win.show()

    sys.exit(app.exec_()) #carpiya basildigini sistemi kapatacak


exeapp()