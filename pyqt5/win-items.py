import sys # komut satiriyla iletişimi sagalyacak
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication , QMainWindow , QToolTip
from PyQt5.QtGui import QIcon




def window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setWindowTitle('First App') 
    win.setGeometry(450,200,500,400)
    win.setWindowIcon(QIcon('wrench.png'))
    win.setToolTip('My tool tip')


    lbl_name = QtWidgets.QLabel(win) # label i window a atar
    lbl_name.setText('Adiniz : ') # label a metin yazmani saglar
    lbl_name.move(50,30) # label i konmlandırır

    lbl_surname = QtWidgets.QLabel(win)
    lbl_surname.setText('Soy Adiniz : ')
    lbl_surname.move(50,70)

    txt_name = QtWidgets.QLineEdit(win) # bu field a denk geliyor javadaki 
    txt_name.move(110,30)

    txt_sname = QtWidgets.QLineEdit(win) # bu field a denk geliyor javadaki 
    txt_sname.move(110,70)

    def clicked():
        print('Butona Tiklandi  Name : '+txt_name.text() + ' Surname : '+txt_sname.text()) # line daki veriyi alir

    btn_save = QtWidgets.QPushButton(win) # button 
    btn_save.setText('Kaydet')
    btn_save.move(110,110)
    btn_save.clicked.connect(clicked)

    

    win.show()
    sys.exit(app.exec_()) #carpiya basildigini sistemi kapatacak


window()