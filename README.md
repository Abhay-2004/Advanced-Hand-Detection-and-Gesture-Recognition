###Advanced Hand Detection and Gesture Recognition

This project implements a real-time hand detection and gesture recognition system using Python, OpenCV, and MediaPipe. The system detects both left and right hands and tracks hand landmarks for various gestures. Additional functionalities include gesture-based interactions for future extensibility.

Features

	•	Real-Time Hand Detection: Identifies hands in live video streams using MediaPipe.
	•	Landmark Visualization: Draws connections between hand landmarks for each detected hand.
	•	Left and Right Hand Identification: Differentiates between left and right hands.
	•	Gesture Recognition Framework (Extendable): Can be extended to recognize specific gestures for controlling external systems.
	•	Optimized for Performance: Fine-tuned for real-time processing using low-latency algorithms.
	•	Future Expansion: Gesture-based control functionalities can be added (e.g., using hand gestures to control media playback or adjust volume).

Requirements

	•	Python 3.x
	•	OpenCV
	•	MediaPipe

Installation

	1.	Clone the repository:
    git clone https://github.com/Abhay-2004/Advanced-Hand-Detection-and-Gesture-Recognition.git
    2. cd Advanced-Hand-Detection-and-Gesture-Recognition


	2.	Install dependencies:
    pip install opencv-python mediapipe protobuf


	3.	Run the script:
    python hand_detection.py



Usage

This project captures video through the webcam and performs real-time hand detection. Detected hands and their landmarks are displayed on the screen along with the hand type (Left/Right). The system is capable of being extended to recognize gestures.

Commands:

	•	Press ‘q’ to quit the program.
	•	The program can be extended to recognize and control actions based on hand gestures.

Extending Gesture Recognition:

	•	Currently, the script includes a framework for recognizing gestures (e.g., pinch gesture). You can easily add your own gestures by adding more conditions in the gesture_recognition function using the detected hand landmarks.

Code Breakdown

detect_hands(frame):

This function detects hands and draws landmarks on the frame. It also calls gesture_recognition to identify specific hand gestures.

display_hand_type(frame, label):

This function displays whether the detected hand is left or right.

gesture_recognition(hand_landmarks, label):

This is a base function for recognizing hand gestures. The example includes a “pinch” gesture when the thumb and index finger are close to each other.

distance(point1, point2):

Calculates the Euclidean distance between two points, used to detect gestures like pinching.

Future Development

	•	Gesture Control for Media: Implement gesture-based controls for media players or presentations.
	•	Hand Tracking for Virtual Mouse Control: Extend the project to simulate mouse control based on hand movement.
	•	Custom Gestures: Add more hand gestures and actions, such as swipes, clicks, and zooming.

