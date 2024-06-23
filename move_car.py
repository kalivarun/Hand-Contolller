import cv2
import mediapipe as mp
import pyautogui as pi
import time

hand_hand = mp.solutions.hands.Hands()
drawing = mp.solutions.drawing_utils
screen_width, screen_height = pi.size()

# Define a threshold to trigger the arrow key press
THRESHOLD = 10  # Adjust this value based on your needs
is_pressed = False

def press_up_and_right():
    pi.keyDown('up')
    pi.keyDown('right')

def release_up_and_right():
    pi.keyUp('up')
    pi.keyUp('right')

def press_up_and_left():
    pi.keyDown('up')
    pi.keyDown('left')

def release_up_and_left():
    pi.keyUp('up')
    pi.keyUp('left')    

def cam():
    global is_pressed  # Declare is_pressed as a global variable
    cap = cv2.VideoCapture(0)
    prev_finger_x = 0

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

                # Get the x-coordinate of the index finger (landmark 8)
                finger_x = int(landmarks[8].x * frame_width)

                # Check the movement of the index finger
                finger_movement = finger_x - prev_finger_x

                # Adjust the threshold based on your needs
                if finger_movement > THRESHOLD:
                    press_up_and_right()
                    is_pressed = True
                elif finger_movement < -THRESHOLD:
                    press_up_and_left()
                    is_pressed = True
                elif is_pressed:
                    release_up_and_right()
                    release_up_and_left()
                    is_pressed = False

                prev_finger_x = finger_x

        else:
            if is_pressed:
                release_up_and_right()
                release_up_and_left()
                is_pressed = False

        cv2.imshow('Virtual gamepad', frame)
        cv2.waitKey(1)

# Run the camera function
cam()
