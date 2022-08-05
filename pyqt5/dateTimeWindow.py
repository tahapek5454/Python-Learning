from PyQt5 import QtWidgets
import sys
from _dateTime import Ui_MainWindow
from PyQt5.QtCore import QDate , QDateTime , QTime


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.calculate)
    
    def calculate(self):
        start = self.ui.dateStart.date()
        end = self.ui.dateEnd.date()

        print(start,end)

        print('Days in mounth {}'.format(start.daysInMonth()))
        print('Days in year {}'.format(start.daysInYear()))

        print('Diffrent between two date {}'.format(start.daysTo(end)))

        print('Simdiki zaman ',end=' ')
        print(QDate.currentDate().getDate())


def app():
    app = QtWidgets.QApplication(sys.argv)

    win = Window()

    win.show()

    sys.exit(app.exec_())


app()