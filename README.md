# Hand Gesture-Based Volume Control using OpenCV and MediaPipe

This Python project uses OpenCV, MediaPipe, and PyAutoGUI to control the system volume based on hand gestures captured through the webcam. It detects the distance between your index finger tip and thumb base, and adjusts the system vHand Gesture-Based Volume Control using OpenCV and MediaPipeolume accordingly.

# Features
Real-time hand gesture detection using MediaPipe

Volume increases when the distance between index finger tip and thumb is large

Volume decreases when the distance is small

Visual feedback via circles and connecting lines on the detected hand

Works on any system with a webcam and Python installed

# How It Works
Uses OpenCV to capture video frames.

MediaPipe Hands model identifies 21 landmarks per hand.

The script tracks:

Landmark 8: Index finger tip

Landmark 4: Thumb tip (or base)

The Euclidean distance between these landmarks determines the volume control:

Distance > 50 → Volume Up

Distance ≤ 50 → Volume Down

# Dependencies 
pip install opencv-python mediapipe pyautogui





