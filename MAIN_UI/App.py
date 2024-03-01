import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from pyqtspinner import *
from time import *
from random import *
import threading


# ==============
# -- settings --
# ==============

win_width = 960
win_height = 640

font = QFont()
font.setFamily("AppleGothic")
greetings = ["Welcome Back", "Good Day", "Greetings", "Welcome to Bionic", "Glad to see you"]

username = "SoftwareTesterUser"


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
        file_path = "/Users/stevenmu/Documents/GitHub/Bionic/MAIN_UI/resources/startup.wav"
        url = QUrl.fromLocalFile(file_path)
        content = QMediaContent(url)
        self.audio_player.setMedia(content)
        self.audio_player.play()
        
        # show main interface
        self.showMainInterface()
        

    # -- create and show the main interface
    def showMainInterface(self):
        
        # text labels
        self.greeting_message = QLabel(self)
        self.greeting_message.setText( greetings[randint(0, 4)] + ", " + username ) 
        font.setPointSize(23)
        self.greeting_message.setFont(font)
        self.greeting_message.move( 40, 30 )
        self.greeting_message.setVisible(True)
        
        # buttons for calibration / library
        self.library_button = QPushButton('Library', self)
        self.library_button.clicked.connect(self.blank)
        self.library_button.setGeometry(25, 70, 100, 40)
        self.library_button.setStyleSheet("background-color: transparent; border: none; color: black; font-size: 16px; text-decoration: underline;")
        self.library_button.show()

        self.calibration_button = QPushButton('Calibration', self)
        self.calibration_button.clicked.connect(self.calibrationSequence)
        self.calibration_button.setGeometry(175, 70, 120, 40)
        self.calibration_button.setStyleSheet("QPushButton { font-size: 16px; } QPushButton:hover { background-color: lightgreen; }")

        self.calibration_button.show()
        
        # - games
        # game 1
        self.game_1 = QPushButton("", self) 
        self.game_1.setGeometry(35, 120, 135, 135) 
        self.game_1.clicked.connect(lambda: self.showBigBoard("./resources/test_desc.png", "RhythmAvenue", "Conquer the music, using your fingers.")) 
        self.game_1.setStyleSheet("border-image: url(./resources/logo.png);")
        self.game_1.enterEvent = lambda event: self.game_1.setStyleSheet("border-image: url(./resources/logo.png); border: -35px solid yellow;")
        self.game_1.leaveEvent = lambda event: self.game_1.setStyleSheet("border-image: url(./resources/logo.png);")
        self.game_1.show()
        
        self.game_1_label = QLabel(self)
        self.game_1_label.setText( "Rhythm Avenue" ) 
        font.setPointSize(12)
        self.game_1_label.setFont(font)
        self.game_1_label.move( 59, 265 )
        self.game_1_label.setVisible(True)
        
        
        # game 2
        self.game_2 = QPushButton("", self) 
        self.game_2.setGeometry(200, 120, 135, 135) 
        self.game_2.clicked.connect(lambda: self.showBigBoard("./resources/test_desc.png", "Snake", "Classic games from decades ago, with a new twist")) 
        self.game_2.setStyleSheet("border-image: url(./resources/logo.png);")
        self.game_2.enterEvent = lambda event: self.game_2.setStyleSheet("border-image: url(./resources/logo.png); border: -35px solid yellow;")
        self.game_2.leaveEvent = lambda event: self.game_2.setStyleSheet("border-image: url(./resources/logo.png);")
        self.game_2.show()
        
        self.game_2_label = QLabel(self)
        self.game_2_label.setText( "Snake" ) 
        font.setPointSize(12)
        self.game_2_label.setFont(font)
        self.game_2_label.move( 249, 265 )
        self.game_2_label.setVisible(True)
    
    
    # def mousePressEvent(self, event):
    #     # Check if the click occurred on a game button
    #     if not any(button.underMouse() for button in [self.game_1, self.game_2]):
    #         # Call clearBigBoard when the background is clicked
    #         self.clearBigBoard()

    #         # Re-enable the buttons after a click elsewhere
    #         self.game_1.setEnabled(True)
    #         self.game_2.setEnabled(True)

    # ======================
    # -- Helper functions --
    # ======================

    # -- set the background
    def setBackgroundImage(self, image_path):
        palette = self.palette()
        palette.setBrush(self.backgroundRole(), QBrush(QPixmap(image_path)))
        self.setPalette(palette)
    
    # -- runs the calibration sequence (seperate executable file)    
    def calibrationSequence(self):
        print("button pressed")
    
    # -- runs the specific game (seperate executable file)    
    def runGame(self, game_name):
        print("button pressed" + game_name)
    
    
    def blank(self):
        return
    
    
    # -- used for showing/hiding the big board 
    def showBigBoard(self, image_path, title, description):
        
        # show the background image
        self.image_label = QLabel(self)
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap)
        self.image_label.setGeometry(0, 450, pixmap.width(), pixmap.height())
        self.image_label.setVisible(True)
        
        # show the title
        self.big_board_title = QLabel(self)
        self.big_board_title.setText( title ) 
        font.setPointSize(26)
        self.big_board_title.setFont(font)
        self.big_board_title.move( 20, 480 )
        self.big_board_title.setVisible(True)  
        
        # show the description
        self.big_board_desc = QLabel(self)
        self.big_board_desc.setText( description ) 
        font.setPointSize(12)
        self.big_board_desc.setFont(font)
        self.big_board_desc.move( 20, 515 )
        self.big_board_desc.setVisible(True) 
        
        # start button
        self.start = QPushButton("Start", self)
        self.start.setStyleSheet("QPushButton { font-size: 16px; } QPushButton:hover { background-color: lightgreen; }")
        self.start.clicked.connect(lambda: self.runGame(title))
        self.start.setGeometry(800, 480, 135, 50) 
        self.start.show()
        
        # # disable double click
        # sender_button = self.sender()
        # sender_button.setEnabled(False)


    # def clearBigBoard(self):
    #     self.big_board_desc.clear()
    #     self.big_board_title.clear()
    #     self.image_label.clear()
