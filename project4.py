import cv2
import cv2.data
import numpy as np

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start video capture from the webcam
video_capture = cv2.VideoCapture(0)

# Check if the video capture object was successfully created
if not video_capture.isOpened():
    print("Error: could not access the webcam")
    exit()

# Main loop to process each video frame
while True:
    ret, frame = video_capture.read()

    if not ret:
        print("Error: unable to read frame from webcam")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('Face Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
