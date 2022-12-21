import cv2
import numpy as np
import text_to_speech as tsp
import winsound
# Import deepface library
from deepface import DeepFace

# Import haarcascade file for face detection
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


def endSound():
    winsound.Beep(600, 300)
    winsound.Beep(600, 400)
    winsound.Beep(400, 500)

def faceEmotionDetection():
    
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
    cap = cv2.VideoCapture(0)
    
    # Check if webcam opened correctly
    if not cap.isOpened():
        cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise IOError('Cannot open webcam')
      
    count = 0  
    while True:
        ret, frame = cap.read()
        result = DeepFace.analyze(frame, actions = ['emotion'], enforce_detection=False, detector_backend='opencv', prog_bar=False)
        
        if result['dominant_emotion'] == 'angry':
            count += 1
        
        if count == 3:
            tsp.text2speech("Hey, You seems a little bit stressed. Why don't we take a break and continue later")
            tsp.text2speech("You are already doing a good job")
            tsp.text2speech("Let's meet up for a lesson later. Good Bye!")
            count = 0
            
            # End program
            endSound()
        
        visualizeEmotion(frame, result)
        
        cv2.imshow('Resized_Window', frame)
        
        if cv2.waitKey(2) & 0xFF == ord('w'):
            print("Stopping Emotion Detection....")
            break
            
    cap.release()
    cv2.destroyAllWindows()
    

