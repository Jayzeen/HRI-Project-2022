import text_to_speech as tsp
import speech_to_text as stt
import time
import control_robot as cr


def MouthExerciseLesson():
    
    tsp.text2speech("Hey there. So let's start the guided mouth exercises now")
    tsp.text2speech("Take a few minutes to get ready to start.")
    time.sleep(2)
    while True:
        userResponse = stt.takeCommand()
        
        if "start" in userResponse:
            tsp.text2speech2("Okay now, Open your jaw as wide without too hard")
            time.sleep(4)
            
            tsp.text2speech2("Hold the position and lift their tongue to the roof of your mouth")
            time.sleep(3)
            tsp.text2speech("Okay! You are doing a Good Job!")
            time.sleep(5)
            
            tsp.text2speech2("Now, Continue touching the roof of your mouth with the tip of your tongue and")
            tsp.text2speech2("move the tip towards the back of the mouth ")
            tsp.text2speech2("Hold the position for a few seconds")
            time.sleep(5)
            
            tsp.text2speech2("Next, stretch your tongue out of your mouth as if you were trying to touch your chin. ")
            tsp.text2speech2("Hold this position for a few seconds as well.")
            time.sleep(3)
            
            tsp.text2speech("Okay! Good Job!")
            flag = True
            if flag:
                try:
                    cr.robot_listen()
                    flag = False
                except:
                    pass 
            tsp.text2speech("Now repeat the above steps again and again for a few minutes")
              
        elif "bye" in userResponse:
            tsp.text2speech("Good bye! Let's meet again")
            break
        elif userResponse == "":
            continue
        else :
            tsp.text2speech("i didn't quite catch that. Could you please repeat it again? Thank you!'")
            continue
        
        time.sleep(1)