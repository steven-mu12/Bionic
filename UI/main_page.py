import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from PyQt5.QtGui import QIcon


current_time = QTime.currentTime().toString(Qt.DefaultLocaleLongDate)[:11]


class MainScreen(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()



    def initUI(self):

        self.resize(960, 640)
        self.center()

        self.setWindowTitle('Bionic Engine')
        self.setWindowIcon(QIcon('resources/web.png'))
        
        greeting = QLabel()
        greeting.setText("Hello World")
        greeting.setAlignment(Qt.AlignCenter)
        vbox.addStretch()

        
        vbox = QVBoxLayout()
        vbox.addWidget(greeting)

        self.show()

    
    # member methods
    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())



def main():

    app = QApplication(sys.argv)
    run = MainScreen()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()