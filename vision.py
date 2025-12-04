import cv2
from cvzone.HandTrackingModule import HandDetector
import time

# Initialize the webcam
# Try camera index 0 first, if fails try 1
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if not cap.isOpened():
    print("Camera 0 failed, trying camera 1...")
    cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("ERROR: Cannot access camera!")
    print("Please check:")
    print("1. Camera permissions in System Settings")
    print("2. No other app is using the camera")
    exit()

cap.set(3, 1280)  # Width
cap.set(4, 720)   # Height

print(f"Camera opened successfully!")

# Initialize the hand detector
# detectionCon: minimum detection confidence (0-1)
# maxHands: maximum number of hands to detect
detector = HandDetector(detectionCon=0.7, maxHands=2)

# For FPS calculation
pTime = 0

print("Hand Tracking Started!")
print("Press 'q' to quit")
print("Show your hand(s) to the camera...")

while True:
    # Read frame from webcam
    success, img = cap.read()
    
    if not success:
        print("Failed to grab frame")
        break
    
    # Find hands in the image
    hands, img = detector.findHands(img)
    
    # If hands are detected
    if hands:
        for hand in hands:
            # Get hand information
            handType = hand["type"]  # "Left" or "Right"
            lmList = hand["lmList"]  # List of 21 landmark points
            bbox = hand["bbox"]      # Bounding box around hand
            center = hand["center"]  # Center of hand
            
            # Display hand type on screen
            cv2.putText(img, f'{handType} Hand', 
                       (bbox[0], bbox[1] - 10),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            
            # Display number of landmarks detected
            cv2.putText(img, f'Landmarks: {len(lmList)}', 
                       (bbox[0], bbox[1] - 40),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)
    
    # Calculate and display FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    
    # Display instructions
    cv2.putText(img, 'Press Q to quit', (10, img.shape[0] - 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
    
    # Show the image
    cv2.imshow("Hand Tracking - Basic Visualization", img)
    
    # Break loop on 'q' press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
print("Hand tracking stopped.")