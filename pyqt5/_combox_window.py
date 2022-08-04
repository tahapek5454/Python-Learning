
from PyQt5 import QtWidgets
import sys
from _combox import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.comboBox.addItem('Turkiye')

        self.ui.btnLoad.clicked.connect(self.loadItems)
        self.ui.btnGet.clicked.connect(self.getItem)

        self.ui.comboBox.currentIndexChanged.connect(self.SelectedIndex) # anlik degisen indexi gonderir
        #Changed[str] dersen text gelir
    
    def loadItems(self):

        liste = ['Ingiltere','Fransa','ABD']

        self.ui.comboBox.addItems(liste)
    
    def getItem(self):

        result = self.ui.comboBox.currentText()
        index = self.ui.comboBox.currentIndex()

        self.ui.lbl.setText(str(index)+' '+result)

        count = self.ui.comboBox.count() # bize sayiyi dondurur

        for i in range(count):
            print(self.ui.comboBox.itemText(i)) # tum hepsini index numrasina gore aliriz
        
    def SelectedIndex(self,index):
        print(index)




def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()

    win.show()

    sys.exit(app.exec_())


app()