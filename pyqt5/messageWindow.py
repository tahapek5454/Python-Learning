from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox  
from _messagedialog import Ui_MainWindow
import sys


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.kisaYol)

    def showDialog(self):
        msg = QMessageBox()

        msg.setWindowTitle('Close App')
        msg.setText('Are you sure Want this')

        msg.setIcon(QMessageBox.Warning) # cikan gorseli ayarlama

        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore) #buton atama

        msg.setDefaultButton(QMessageBox.Cancel) # alternatif butonu seçiyor

        msg.setDetailedText('Detaylar acikalmaalar yazilir')
    
        msg.setDefaultButton(QMessageBox.Cancel) # alternatif butonu seçiyor

        msg.buttonClicked.connect(self.popup_show)

        x = msg.exec_() # calistirma exe
    

    def popup_show(self , i):

        text = i.text()

        if text == 'OK':
            print('Okey....')
            QtWidgets.qApp.quit() # uygulamayı kapatır
        
        elif text == 'Cancel':
            print('Cancel .... ')
        else :
            print('Ignore ... ')
    
    def kisaYol(self):

        result = QMessageBox.question(self,'exit app','Are you sure',QMessageBox.Ok | QMessageBox.Cancel,QMessageBox.Cancel)

        if result == QMessageBox.Ok:
            print('Cikis yapiiliyor')
            QtWidgets.qApp.quit()


def app():

    app = QtWidgets.QApplication(sys.argv)

    win = Window()

    win.show()
    
    sys.exit(app.exec_())

app()