import sys # komut satiriyla iletişimi sagalyacak
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication , QMainWindow , QToolTip
from PyQt5.QtGui import QIcon




class Mywindow(QMainWindow):
    
    def __init__(self) -> None:
        super(Mywindow,self).__init__()

        self.setWindowTitle('First App') 
        self.setGeometry(450,200,500,400)
        self.setWindowIcon(QIcon('wrench.png'))
        self.setToolTip('My tool tip')
        self.initUI()
    
    def initUI(self):
        self.lbl_name = QtWidgets.QLabel(self) # label i window a atar
        self.lbl_name.setText('Adiniz : ') # label a metin yazmani saglar
        self.lbl_name.move(50,30) # label i konmlandırır

        self.lbl_surname = QtWidgets.QLabel(self)
        self.lbl_surname.setText('Soy Adiniz : ')
        self.lbl_surname.move(50,70)

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.move(110,150)
        self.lbl_result.resize(300,32)

        self.txt_name = QtWidgets.QLineEdit(self) # bu field a denk geliyor javadaki 
        self.txt_name.move(110,30)
        self.txt_name.resize(200,32) # line inboyuttunu belirler

        self.txt_sname = QtWidgets.QLineEdit(self) # bu field a denk geliyor javadaki 
        self.txt_sname.move(110,70)
        self.txt_sname.resize(200,32)

   
        self.btn_save = QtWidgets.QPushButton(self) # button 
        self.btn_save.setText('Kaydet')
        self.btn_save.move(110,110)
        self.btn_save.clicked.connect(self.clicked)

        
    
    def clicked(self):
        self.lbl_result.setText('Name : '+self.txt_name.text() + ' Surname : '+self.txt_sname.text()) # line daki veriyi alir


        


def window():
    app = QApplication(sys.argv)
    win = Mywindow()
    win.show()
    sys.exit(app.exec_()) #carpiya basildigini sistemi kapatacak


window()