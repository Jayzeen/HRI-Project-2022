import text_to_speech as tsp
import speech_to_text as stt
import time

def FacialMuscleExerciseLesson():
    
    tsp.text2speech("Hey there. So let's start the guided Facial Muscle exercises now")
    tsp.text2speech("Take a few minutes to get ready to start.")
    time.sleep(2)
    while True:
        userResponse = stt.takeCommand()
        
        if "start" in userResponse:
            tsp.text2speech2("First we are going to try some Loud vowel Pronouncements")
            time.sleep(2)
            tsp.text2speech2("Speak ,A, sound loudly and stretching your face with letter sound, continue it for five seconds")
            time.sleep(6)
            
            tsp.text2speech2("Speak ,E, sound loudly and stretching your face with letter sound, continue it for five seconds")
            time.sleep(6)
            tsp.text2speech("Okay! You are doing a Good Job!")
            time.sleep(3)
            
            tsp.text2speech2("Speak ,I, sound loudly and stretching your face with sound, continue it for five seconds. ")
            time.sleep(6)
            tsp.text2speech("Great! keep it up!")
            time.sleep(3)
            
            tsp.text2speech2("Speak ,O, sound loudly and stretching your face with letter sound, continue it for five seconds. ")
            time.sleep(6)
            
            tsp.text2speech2("Speak ,U, sound loudly and stretching your face with letter sound, continue it for five seconds. ")
            time.sleep(6)
            
            tsp.text2speech("wow! now that is some damn good pronounciations!")
            tsp.text2speech("Now relax your mouth and repeat this six times")
              
        elif "bye" in userResponse:
            tsp.text2speech("Good bye! Let's meet again")
            break
        elif userResponse == "":
            continue
        else :
            tsp.text2speech("i didn't quite catch that. Could you please repeat it again? Thank you!'")
            continue
        
        time.sleep(1)