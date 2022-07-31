# to Download
# pip install pyqt5
# pip install pyqt5-tools

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

    win.show()
    sys.exit(app.exec_()) #carpiya basildigini sistemi kapatacak


window()