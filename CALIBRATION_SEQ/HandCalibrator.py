import cv2
import mediapipe as mp
# import RPi.GPIO as GPIO
from time import sleep


class HandCalibrator:
    
    # -- constructor for initializations
    def __init__(self):
        self.mp_drawing = mp.solutions.drawing_utils
        self.mphands = mp.solutions.hands
        self.hands = self.mphands.Hands()
        self.cap = cv2.VideoCapture(0)

        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(14, GPIO.OUT)
        # GPIO.setup(15, GPIO.OUT)
        
    
    # -- height calibration method
    def calibrate_height(self, y_coord):
        difference = 0.8 - y_coord
        time_to_move = abs(difference) / 0.05
        
        # if difference > 0:
        #     GPIO.output(15, GPIO.HIGH)
        #     GPIO.output(14, GPIO.LOW)
        # elif difference < 0:
        #     GPIO.output(15, GPIO.LOW)
        #     GPIO.output(14, GPIO.HIGH)
        
        # GPIO.output(15, GPIO.LOW)
        # GPIO.output(14, GPIO.LOW)


    # -- run the main program
    def run(self):
        
        while True:
            ret, image = self.cap.read()
            image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
            results = self.hands.process(image)
            hand_detected = False

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    self.mp_drawing.draw_landmarks(image, hand_landmarks, self.mphands.HAND_CONNECTIONS)
                    landmarks = [landmark for landmark in hand_landmarks.landmark]
                    
                    hand_detected = True
                    current_wrist_x = landmarks[0].x
                    current_wrist_y = landmarks[0].y

                    # display instructions
                    self.display_instructions(image, current_wrist_x, hand_detected)

                    # calibrate height if the hand is centered
                    if 0.4 <= current_wrist_x <= 0.6:
                        self.calibrate_height(current_wrist_y)
                        break
            
            # if no hand, tell use to display hand
            if not hand_detected:
                self.display_instructions(image, None, hand_detected)

            # exit condition
            cv2.imshow("Handtracker", cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()


    # -- used for the GUI to display info to users
    def display_instructions(self, image, current_wrist_x, hand_detected):
        if hand_detected:
            if current_wrist_x > 0.6:
                self.display_text(image, "Hand Detected", "Please slowly move your hand to the LEFT")
            elif current_wrist_x < 0.4:
                self.display_text(image, "Hand Detected", "Please slowly move your hand to the RIGHT")
            else:
                self.display_text(image, "Calibration Sequence", "Please do not move your hand")
        else:
            self.display_text(image, "Welcome To The Calibration Sequence", "No hand detected. Place your hand in front of the camera.")


    def display_text(self, image, header, instruction):
        cv2.putText(image, header, (300, 400), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 5, cv2.LINE_AA)
        cv2.putText(image, instruction, (300, 475), cv2.FONT_HERSHEY_SIMPLEX, 1.25, (0, 255, 0), 3, cv2.LINE_AA)
