import cv2
import mediapipe as mp
from google.protobuf.json_format import MessageToDict

# Initialize MediaPipe Hands model and drawing utilities
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

# Setup Hands model parameters
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    model_complexity=1,
    min_detection_confidence=0.75,
    min_tracking_confidence=0.75
)

# Initialize video capture from webcam
cap = cv2.VideoCapture(0)

def detect_hands(frame):
    """ Detect and display hand landmarks on the frame. """
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)
    
    hand_detected = False
    
    if results.multi_hand_landmarks:
        hand_detected = True
        for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            # Draw landmarks on the hand
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Identify if the hand is left or right
            label = MessageToDict(handedness)['classification'][0]['label']
            display_hand_type(frame, label)
            
            # Implement additional gesture recognition
            gesture_recognition(hand_landmarks, label)

    return frame, hand_detected

def display_hand_type(frame, label):
    """ Display hand type (Left/Right) on the frame. """
    if label == 'Left':
        cv2.putText(frame, 'Left Hand', (20, 50), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0, 255, 0), 2)
    elif label == 'Right':
        cv2.putText(frame, 'Right Hand', (460, 50), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0, 255, 0), 2)

def gesture_recognition(hand_landmarks, label):
    """ Framework for recognizing gestures based on hand landmarks. """
    # Sample framework for future gesture recognition functionality
    finger_positions = []
    for id, lm in enumerate(hand_landmarks.landmark):
        # Collect the positions of each landmark
        finger_positions.append((lm.x, lm.y))

    # Example gesture: thumb and index finger close = 'Pinch' gesture
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    
    if distance(thumb_tip, index_tip) < 0.05:  # Arbitrary threshold
        print(f"{label} Hand Gesture: Pinch")

def distance(point1, point2):
    """ Calculate the Euclidean distance between two points. """
    return ((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2) ** 0.5

# Main loop
while cap.isOpened():
    success, frame = cap.read()
    
    if not success:
        print("Ignoring empty frame.")
        continue

    frame = cv2.flip(frame, 1)

    # Detect hands and get modified frame
    frame, hand_detected = detect_hands(frame)

    # Show the frame
    cv2.imshow('Hand Detection and Gesture Recognition', frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam and close windows
cap.release()
cv2.destroyAllWindows()