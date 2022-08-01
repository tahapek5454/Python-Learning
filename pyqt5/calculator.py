import sys # komut satiriyla iletişimi sagalyacak
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication , QMainWindow , QToolTip
from PyQt5.QtGui import QIcon


class MainForm(QMainWindow):

    def __init__(self):
        super(MainForm,self).__init__()

        self.setWindowTitle('Calculator')
        self.setGeometry(550,150,350,400)
        self.initUI()


    def initUI(self):
        
        self.lbl_sayi1 = QtWidgets.QLabel(self)
        self.lbl_sayi1.setText('Sayi 1 : ')
        self.lbl_sayi1.move(50,30)


        self.txt_sayi1 = QtWidgets.QLineEdit(self)
        self.txt_sayi1.move(120,30)
        self.txt_sayi1.resize(100,32)



        self.lbl_sayi2 = QtWidgets.QLabel(self)
        self.lbl_sayi2.setText('Sayi 2 : ')
        self.lbl_sayi2.move(50,80)

        self.txt_sayi2 = QtWidgets.QLineEdit(self)
        self.txt_sayi2.move(120,80)
        self.txt_sayi2.resize(100,32)

        self.topla_btn = QtWidgets.QPushButton(self)
        self.topla_btn.setText('Topla')
        self.topla_btn.move(120,120)
        self.topla_btn.clicked.connect(self.hesapla)

        self.cikar_btn = QtWidgets.QPushButton(self)
        self.cikar_btn.setText('Cikar')
        self.cikar_btn.move(120,160)
        self.cikar_btn.clicked.connect(self.hesapla)

        self.carp_btn = QtWidgets.QPushButton(self)
        self.carp_btn.setText('Carp')
        self.carp_btn.move(120,200)
        self.carp_btn.clicked.connect(self.hesapla)

        self.bol_btn = QtWidgets.QPushButton(self)
        self.bol_btn.setText('Bol')
        self.bol_btn.move(120,240)
        self.bol_btn.clicked.connect(self.hesapla)

        self.lbl_sonuc = QtWidgets.QLabel(self)
        self.lbl_sonuc.setText('Sonuc : ')
        self.lbl_sonuc.move(120,280)
        self.lbl_sonuc.resize(200,32)
    
    def toplama(self):
        try:
            result = int(self.txt_sayi1.text()) + int(self.txt_sayi2.text())
            self.lbl_sonuc.setText('Sonuc : '+str(result))
        except Exception as ex:
            print('eror',ex)
            self.lbl_sonuc.setText('Sonuc : Yanlis bir islem yaptiniz')
    
    def cikarma(self):
        try:
            result = int(self.txt_sayi1.text()) - int(self.txt_sayi2.text())
            self.lbl_sonuc.setText('Sonuc : '+str(result))
        except Exception as ex:
            print('eror',ex)
            self.lbl_sonuc.setText('Sonuc : Yanlis bir islem yaptiniz')
    
    def carpma(self):
        try:
            result = int(self.txt_sayi1.text()) * int(self.txt_sayi2.text())
            self.lbl_sonuc.setText('Sonuc : '+str(result))
        except Exception as ex:
            print('eror',ex)
            self.lbl_sonuc.setText('Sonuc : Yanlis bir islem yaptiniz')
    
    def bolme(self):
        try:
            result = int(self.txt_sayi1.text()) / int(self.txt_sayi2.text())
            self.lbl_sonuc.setText('Sonuc : '+str(result))
        except Exception as ex:
            print('eror',ex)
            self.lbl_sonuc.setText('Sonuc : Yanlis bir islem yaptiniz')
    

    # ya da soyle bir yontem izlenir

    def hesapla(self):
        sender = self.sender() # bize tıklanan butonu gonderir onemli

        if sender.text() == 'Topla': #tıklanan butonun textini aldik
            self.toplama()
        
        elif sender.text() == 'Cikar': # sender == 'Cikar' da olur
            self.cikarma()
        
        elif sender.text() == 'Carp':
            self.carpma()
        
        elif sender.text() == 'Bol':
            self.bolme()



def window():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_()) #carpiya basildigini sistemi kapatacak


window()