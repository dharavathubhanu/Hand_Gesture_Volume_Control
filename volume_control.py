import cv2
import mediapipe as mp
import pyautogui

# Initialize the variables to hold hand landmark coordinates
x1 = y1 = x2 = y2 = 0

# Start the webcam
webcam = cv2.VideoCapture(0)

# Initialize MediaPipe Hands model
my_hands = mp.solutions.hands.Hands()

# Drawing utilities for hand landmarks
drawing_utils = mp.solutions.drawing_utils

# Infinite loop to continuously capture webcam frames
while True:
    # Read a frame from the webcam
    _, image = webcam.read()

    # Flip the image horizontally for mirror effect (like looking in a mirror)
    image = cv2.flip(image, 1)

    # Get the dimensions of the frame
    frame_height, frame_width, _ = image.shape

    # Convert the image to RGB (MediaPipe expects RGB format)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process the image and detect hands
    output = my_hands.process(rgb_image)

    # Get landmarks for each detected hand
    hands = output.multi_hand_landmarks

    # If hands are detected, loop through each hand
    if hands:
        for hand in hands:
            # Draw hand landmarks on the image
            drawing_utils.draw_landmarks(image, hand)

            # Get the landmarks of the hand
            landmarks = hand.landmark

            # Loop through each landmark in the hand
            for id, landmark in enumerate(landmarks):
                # Convert the normalized coordinates to pixel coordinates
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)

                # If the landmark is the tip of the index finger (id == 8)
                if id == 8:
                    # Draw a circle on the tip of the index finger
                    cv2.circle(img=image, center=(x, y), radius=8, color=(0, 255, 255), thickness=3)

                    # Store the coordinates of the index finger tip
                    x1 = x
                    y1 = y

                # If the landmark is the base of the thumb (id == 4)
                if id == 4:
                    # Draw a circle on the base of the thumb
                    cv2.circle(img=image, center=(x, y), radius=8, color=(0, 0, 255), thickness=3)

                    # Store the coordinates of the base of the thumb
                    x2 = x
                    y2 = y

                # Calculate the distance between the tip of the index finger and the base of the thumb
                dist = ((x2 - x1)**2 + (y2 - y1)**2)**0.5 // 4

                # Draw a line between the index finger tip and thumb base
                cv2.line(image, (x1, y1), (x2, y2), color=(0, 255, 0), thickness=5)

                # If the distance between the two points is greater than 50, increase volume
                if dist > 50:
                    pyautogui.press('volumeup')
                else:
                    # If the distance is less than or equal to 50, decrease volume
                    pyautogui.press('volumedown')

    # Display the image with hand landmarks
    cv2.imshow('Hand Volume Control using Python', image)

    # Exit the loop if the 'ESC' key is pressed
    key = cv2.waitKey(10)
    if key == 27:
        break

# Release the webcam and close all OpenCV windows
webcam.release()
cv2.destroyAllWindows()
