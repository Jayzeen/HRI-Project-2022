import speech_recognition as sr
import text_to_speech as tsp
import speech_to_text as stt
import time

from lessons import BreathingLesson as bl
from lessons import MouthLesson as ml
from lessons import FacialMuscleLesson as fl
from lessons import SpeakingLesson as sl


def StartTrainingPlan():
    
    tsp.text2speech("Hello Friend. Shall we start today's lesson then")
    tsp.text2speech("Today's lesson plan includes Breathing exercises, mouth exercises and facial muscles exercises")
    tsp.text2speech("Which one do you wanna try?")
    while True:
        userResponse = stt.takeCommand()
        
        if "breathing exercises" in userResponse:
            tsp.text2speech("Okay, Let's start doing some breathing exercises")
            bl.BreathingExerciseLesson()
    
        elif "mouth exercises" in userResponse:
            tsp.text2speech("Great, Let's start doing some mouth exercises")
            ml.MouthExerciseLesson()
            
        elif "facial muscle exercises" in userResponse:
            tsp.text2speech("Very good, Let's start doing some facial muscles exercises")
            fl.FacialMuscleExerciseLesson()
            
        elif "speaking exercises" in userResponse:
            tsp.text2speech("Great choice, Let's start doing some speaking exercises")
            sl.SpeechExerciseLesson()
            
        elif "bye" in userResponse:
            tsp.text2speech("Good bye! Let's meet again")
            break
        elif userResponse == "":
            continue
        else :
            tsp.text2speech("i didn't quite catch that. Could you please repeat it again? Thank you!")
            continue
        
        time.sleep(1)
    