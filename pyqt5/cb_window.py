from PyQt5 import QtWidgets
import sys

from matplotlib.pyplot import text
from cb import Ui_MainWindow


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #self.ui.cb_spor.stateChanged.connect(self.show_state) # direkt seciliken tepkimesini gosterir
        self.ui.btn.clicked.connect(self.getAll)
    

    def getAll(self):
        items = self.ui.groupBox.findChildren(QtWidgets.QCheckBox) # group box icindekileri secer
        result = 'Secili Olanlar \n'
        for cb in items:
            if cb.isChecked():
                result +=  cb.text() + '\n'
        
        self.ui.lbl.setText(result)
            

    
    # def show_state(self,value): #burdaki metoddirekt secili oldu mu gosterir
    #     print(value)



def App():
    app = QtWidgets.QApplication(sys.argv)

    win = MyApp()

    win.show()

    sys.exit(app.exec_())


App()
