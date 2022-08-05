from PyQt5 import QtWidgets
import sys
from _listView import Ui_MainWindow
from PyQt5.QtWidgets import QInputDialog , QLineEdit , QMessageBox


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # load students

        self.loadStudents()

        # add student

        self.ui.addBtn.clicked.connect(self.addStudent)

        # edit student

        self.ui.editBtn.clicked.connect(self.editStudent)

        # remove Student

        self.ui.removeBtn.clicked.connect(self.removeStudent)

        # up Student

        self.ui.upBtn.clicked.connect(self.upStudent)

        # down Student

        self.ui.downBtn.clicked.connect(self.downStudent)

        # exit

        self.ui.exitBtn.clicked.connect(self.close)
    
    def loadStudents(self):

        self.ui.listWidget.addItems(['Ahmet','Taha','Mehmet'])
        
        self.ui.listWidget.setCurrentRow(0) # secili row u secersin
    
    def addStudent(self):
        text , ok = QInputDialog.getText(self,'New Student','Student Name') # bize bir input acar 2 sey dondurur

        if text and ok is not None:

            current_index = self.ui.listWidget.currentRow() #anlik secili indexi verir
            self.ui.listWidget.insertItem(current_index,text) # secili indexe. inci index e ekle

    
    def editStudent(self):

        index = self.ui.listWidget.currentRow() # secili index gelir
        item = self.ui.listWidget.item(index) # indexteki objeyi referans verir

        if item is not None:
            # onceki bilginin de gozukmesi icin ek islemler yaptik 
            text , ok = QInputDialog.getText(self,'Edit Student','Student Name',QLineEdit.Normal,item.text())

            if text and ok is not None:
                item.setText(text)

    
    def removeStudent(self):

        index = self.ui.listWidget.currentRow() # secili index gelir
        item = self.ui.listWidget.item(index) # indexteki objeyi referans verir

        if item is None:
            return
        
        q = QMessageBox.question(self,'Remove Student','Do you want to remove '+item.text(),QMessageBox.Yes | QMessageBox.No)

        if q == QMessageBox.Yes:

            item = self.ui.listWidget.takeItem(index) # objeyi silmek icin kullanilir
            del item


    def upStudent(self):

        index = self.ui.listWidget.currentRow()

        if index != 0:

            item = self.ui.listWidget.takeItem(index)
            self.ui.listWidget.insertItem(index-1,item)
            self.ui.listWidget.setCurrentItem(item)
    
    def downStudent(self):
        index = self.ui.listWidget.currentRow()

        if index != self.maxIndex():
            item = self.ui.listWidget.takeItem(index)
            self.ui.listWidget.insertItem(index+1,item)
            self.ui.listWidget.setCurrentItem(item)


    def maxIndex(self):

        sayi = self.ui.listWidget.count()

        return sayi-1
    
    def sort(self):
        self.ui.listWidget.sortItems()
    
    def close(self):
        quit()

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()

    win.show()

    sys.exit(app.exec_())


app()
