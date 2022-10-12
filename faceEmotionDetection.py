import tensorflow as tf
import cv2
import os
import numpy as np

# Import deepface library
from deepface import DeepFace

# Import haarcascade file for face detection
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to visualize emotion as text in frame
def visualizeEmotion(img,predictions):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = np.array(gray, dtype='uint8')
    faces = faceCascade.detectMultiScale(gray,1.1,4)

    # Draw rectangle
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
        
    # putText method to include text
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,
               predictions['dominant_emotion'],
               (10,100),
               font,
                2,
               (0,0,255),
               3);


# Realtime Emotion detection
cap = cv2.VideoCapture(1)
# Check if webcam opened correctly
if not cap.isOpened():
    cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError('Cannot open webcam')
    
while True:
    ret, frame = cap.read()
    result = DeepFace.analyze(frame, actions = ['emotion'], enforce_detection=False,detector_backend='opencv', prog_bar=True)
    
    visualizeEmotion(frame, result)
    
    cv2.imshow('Original video', frame)
    
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()