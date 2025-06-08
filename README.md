# Hand Gesture-Based Volume Control using OpenCV and MediaPipe

This Python project uses OpenCV, MediaPipe, and PyAutoGUI to control the system volume based on hand gestures captured through the webcam. It detects the distance between your index finger tip and thumb base, and adjusts the system vHand Gesture-Based Volume Control using OpenCV and MediaPipeolume accordingly.

# Features
1. Real-time hand gesture detection using MediaPipe
2. Volume increases when the distance between index finger tip and thumb is large
3. Volume decreases when the distance is small
4. Visual feedback via circles and connecting lines on the detected hand
5. Works on any system with a webcam and Python installed

# How It Works ?
Uses OpenCV to capture video frames.

MediaPipe Hands model identifies 21 landmarks per hand.

The script tracks:

Landmark 8: Index finger tip

Landmark 4: Thumb tip (or base)

The Euclidean distance between these landmarks determines the volume control:

Distance > 50 → Volume Up

Distance ≤ 50 → Volume Down

# How to run ?
1. Ensure your webcam is connected and functioning.

2. Run the script:
python volume_control.py
3.Show your hand to the webcam and move your index finger and thumb apart or together to adjust the system volume.
4.Press ESC to exit.

# Dependencies 
pip install opencv-python mediapipe pyautogui





