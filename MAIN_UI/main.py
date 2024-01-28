
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from pyqtspinner import *
from time import *
from random import *
from App import *



# ==================
# -- Main Program --
# ==================

def main():
    app = QApplication(sys.argv)
    
    # adding icon
    icon = QIcon("./resources/logo.png")  # Replace with the path to your icon file
    app.setWindowIcon(icon)
    
    # building app
    application = App()
    application.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()