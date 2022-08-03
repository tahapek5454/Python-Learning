from PyQt5 import QtWidgets
import sys
from rb import Ui_MainWindow


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.radioTurkey.setChecked(True) # default olarak secili hale getirir
        self.ui.radioTurkce.setChecked(True)

        self.ui.radioABD.toggled.connect(self.onClickedUlke) #secili radio butınu etkinlestirir
        self.ui.radioIng.toggled.connect(self.onClickedUlke)
        self.ui.radioTurkey.toggled.connect(self.onClickedUlke)
        self.ui.radioRusya.toggled.connect(self.onClickedUlke)

        self.ui.radioIngilizce.toggled.connect(self.onClickedDers) #secili radio butınu etkinlestirir
        self.ui.radioMatematik.toggled.connect(self.onClickedDers)
        self.ui.radioTurkce.toggled.connect(self.onClickedDers)
        self.ui.radioFizik.toggled.connect(self.onClickedDers)

        self.ui.btn_ders.clicked.connect(self.getSelectedDers)
        self.ui.btn_ulke.clicked.connect(self.getSelectedUlke)
    

    def onClickedUlke(self):
        rb = self.sender()

        if rb.isChecked():
            print('Secili radio : '+rb.text())
    

    def onClickedDers(self):
        rb = self.sender()

        if rb.isChecked():
            print('Secili radio : '+rb.text())
    
    def getSelectedDers(self):

        liste = self.ui.frame_2.findChildren(QtWidgets.QRadioButton)
        result = 'Secili Dersler \n'
        for i in liste:
            if i.isChecked():
                result += i.text() + '\n'
        
        self.ui.lbl_ders.setText(result)
    

    def getSelectedUlke(self):

        liste = self.ui.frame.findChildren(QtWidgets.QRadioButton)
        result = 'Secili Ulkeler \n'
        for i in liste:
            if i.isChecked():
                result += i.text() + '\n'
        
        self.ui.lbl_ulke.setText(result)

        


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()

    win.show()

    sys.exit(app.exec_())


app()
