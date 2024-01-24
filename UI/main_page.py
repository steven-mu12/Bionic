
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from pyqtspinner import *
from time import *
from random import *


# ==============
# -- settings --
# ==============

win_width = 960
win_height = 640

font = QFont()
font.setFamily("AppleGothic")
greetings = ["Welcome Back", "Good Day", "Greetings"]

username = "TestUser"


# ===========================
# -- application class def --
# ===========================

class App(QWidget):
    
    # -- constructor
    def __init__(self, parent = None):
        super(App, self).__init__(parent)
        
        # initializations
        self.resize( win_width, win_height )
        self.setWindowTitle("Bionic")
        
        # set the background images
        self.setBackgroundImage("./resources/bg.png")
        
        # add main bionic text
        self.intro_label = QLabel(self)
        self.intro_label.setText("Bionic")
        font.setPointSize(18)
        self.intro_label.setFont(font)
        self.intro_label.move( int(win_width/2)-22, int(win_height/2)-40 )
        
        # loading bar
        self.spinner = WaitingSpinner(
            self,
            roundness=99.99,
            fade=75.0,
            radius=6,
            lines=200,
            line_length=4,
            line_width=3,
            speed=1.0
        )
        
        # audio player
        self.audio_player = QMediaPlayer()
        
        # -- STARTUP SECTION
        self.spinner.start()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.startupClear)  # Connect the timeout signal to the clearScreen method
        self.timer.start(randint(3000, 5000))



    # ===================
    # -- Event Methods --
    # ===================
    
    # -- clear the screen for startup
    def startupClear(self):
        self.timer.stop()
        self.intro_label.clear()
        self.spinner.stop()
        
        # play startup sound
        file_path = "/Users/stevenmu/Documents/GitHub/Bionic/UI/resources/startup.wav"
        url = QUrl.fromLocalFile(file_path)
        content = QMediaContent(url)
        self.audio_player.setMedia(content)
        self.audio_player.play()
        
        # show main interface
        self.showMainInterface()
        

    # -- create and show the main interface
    def showMainInterface(self):
        self.greeting_message = QLabel(self)
        self.greeting_message.setText( greetings[randint(0, 2)] + ", " + username ) 
        font.setPointSize(26)
        self.greeting_message.setFont(font)
        self.greeting_message.move( 25, 30 )
        self.greeting_message.setVisible(True)
        
        self.library_button = QPushButton('Button 1', self)
        self.library_button.clicked.connect(self.button1_clicked)
        self.library_button.setGeometry(25, 70, 100, 50)
        self.library_button.show()

        self.settings_button = QPushButton('Button 2', self)
        self.settings_button.clicked.connect(self.button1_clicked)
        self.settings_button.setGeometry(175, 70, 100, 50)
        self.settings_button.show()


    # ======================
    # -- Helper functions --
    # ======================

    # -- set the background
    def setBackgroundImage(self, image_path):
        palette = self.palette()
        palette.setBrush(self.backgroundRole(), QBrush(QPixmap(image_path)))
        self.setPalette(palette)
        
    def button1_clicked(self):
        print("button pressed")


# ==================
# -- Stylesheetas --
# ==================        


# ============
# -- update --
# ============

def main():
    app = QApplication(sys.argv)
    application = App()
    application.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()