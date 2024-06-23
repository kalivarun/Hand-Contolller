import cv2
import mediapipe as mp
import pyautogui as pi 
import math

hand_hand = mp.solutions.hands.Hands()
drawing = mp.solutions.drawing_utils
screen_width, screen_height = pi.size()

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def cam():
    cap = cv2.VideoCapture(0)
    while True:
        _, frame = cap.read()
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_height, frame_width, _ = frame.shape 
        output = hand_hand.process(rgb_frame)
        
        hands = output.multi_hand_landmarks
        if hands:
            for hand in hands:
                drawing.draw_landmarks(frame, hand)
                landmarks = hand.landmark
                x4, y4 = int(landmarks[4].x * frame_width), int(landmarks[4].y * frame_height)
                x8, y8 = int(landmarks[8].x * frame_width), int(landmarks[8].y * frame_height)
                
                # Draw a line connecting landmarks 4 and 8 for visualization
                cv2.line(frame, (x4, y4), (x8, y8), (255, 0, 0), 2)
                
                distance = calculate_distance(x4, y4, x8, y8)
                for id, landmark in enumerate(landmarks):
                  if id == 8:
                    cv2.circle(img=frame, center=(x4, y4), radius=10, color=(0, 255, 255))

                    index_x = (1 - landmarks[4].x) * screen_width
                    index_y = landmarks[4].y * screen_height
                    pi.moveTo(index_x, index_y)

                  elif distance < 30:  # You may need to adjust this threshold based on your testing
                     pi.click()

        cv2.imshow('Virtual Mouse', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

cam()
