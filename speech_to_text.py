import speech_recognition as sr

# ************* FUNCTION TO LISTEN AND CONVERT SPEECH TO TEXT *************
def takeCommand():
      
    r = sr.Recognizer()
    query = ""
    
    try:
         
        with sr.Microphone() as mic:
            print("Listening...")
            r.pause_threshold = 2
            r.adjust_for_ambient_noise(mic, duration=0.2)
            audio = r.listen(mic)
    
            print("Recognizing...")   
            query = r.recognize_google(audio, language ='en-In')
            print(f"User said: {query}")
        
    except Exception as e:   
        pass
     
    return query.lower()