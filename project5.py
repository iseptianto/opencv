import cv2
from fer import FER

emotion_detector = FER()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: unable to read frame from webcam")
        break

    emotions = emotion_detector.detect_emotions(frame)

    if emotions:
        emotion_data = emotions[0]['emotions']
        max_emotion = max(emotion_data, key=emotion_data.get)
        (x, y, w, h) = emotions[0]["box"]
        cv2.putText(frame, max_emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display the resulting frame
    cv2.imshow('Emotion Detector', frame)
    
    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
