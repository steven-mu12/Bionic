import cv2
import mediapipe as mp


# -- initialize mediapipe & start videocapture

mp_drawing = mp.solutions.drawing_utils
mphands = mp.solutions.hands
cap = cv2.VideoCapture(0)
hands = mphands.Hands()


# -- necessary data storage


# -- monitoring video

while True:
    ret, image = cap.read()

    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    if results.multi_hand_landmarks:
        
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mphands.HAND_CONNECTIONS)

            # -- get the positions of landmarks
            landmarks = []
            for landmark in hand_landmarks.landmark:
                landmarks.append(landmark)

            # ---------------------
            # -- gesture recogition 
            # ---------------------
            
            threshold = 0.059 # WHEN BUILDING MAIN, TAKE USER's HAND INTO CONSIDERATION (ask the user to move further/closer and hold touch until good - use ultrasonic sensor for this)
            index_touch = False

            if (abs(landmarks[4].x - landmarks[8].x) <= threshold) and (abs(landmarks[4].y - landmarks[8].y) <= threshold):
                print("INDEX TOUCH")
                
            if (abs(landmarks[4].x - landmarks[12].x) <= threshold) and (abs(landmarks[4].y - landmarks[12].y) <= threshold):
                print("MIDDLE TOUCH")
                
            if (abs(landmarks[20].y > landmarks[9].y)) and (abs(landmarks[20].y > landmarks[13].y)) and (abs(landmarks[20].y > landmarks[5].y)):
                print("PINKY SWING")
            
            if (abs(landmarks[16].y > landmarks[9].y)) and (abs(landmarks[16].y > landmarks[13].y)) and (abs(landmarks[16].y > landmarks[5].y)):
                print("Ring SWING")
            
            
            # ---------------------
            # -- motion recogition 
            # ---------------------
            
            
            
            
            
            # -----------------------------------------------------
            # -- coordinate recogition (for navigating with cursor)
            # -----------------------------------------------------
            
            
            
            
    
    # -- display the frame (for debugging)
    cv2.imshow("Handtracker", cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
