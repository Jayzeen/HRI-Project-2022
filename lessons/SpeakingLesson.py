import text_to_speech as tsp
import speech_to_text as stt
import time
import control_robot as cr


def SpeechExerciseLesson():
    
    tsp.text2speech("Hello. So let's start the Speaking exercises now")
    tsp.text2speech("Take a few minutes to get ready to start.")
    tsp.text2speech("Once you are done with one exercise, please say next to move on to the next exercise")
    time.sleep(2)
    while True:
        userResponse = stt.takeCommand()
        
        if "start" in userResponse:
            tsp.text2speech2("Okay now, Try saying these sentences as clearly as you can without stuttering")
            tsp.text2speech2("Don't be in a hurry. Take as much time as you need")
            time.sleep(4)
            
            tsp.text2speech2("The quick brown fox jumps over the lazy dog")
            time.sleep(10)
            tsp.text2speech("Okay! You are doing a Good Job!")
            time.sleep(5)
            
            tsp.text2speech2("Next sentence")
            time.sleep(2)
            tsp.text2speech2("She sells seashells by the seashore.")
            time.sleep(10)
            tsp.text2speech("Wow! That is amazing!")
            flag = True
            if flag:
                try:
                    cr.robot_listen()
                    flag = False
                except:
                    pass 
            time.sleep(2)
            
            tsp.text2speech("Now repeat the above sentences again and again until you are satisfied with the results")
        elif "next" in userResponse:
            tsp.text2speech2("Okay now let's move on to the next part")
            tsp.text2speech2("Again Don't be in a hurry. Take as much time as you need")
            time.sleep(4)
            
            tsp.text2speech2("Peter Piper picked a peck of pickled peppers")
            time.sleep(10)
            tsp.text2speech("Okay! Well done!")
            time.sleep(5)
            
            tsp.text2speech2("Next sentence")
            time.sleep(2)
            tsp.text2speech2("How now brown cow")
            time.sleep(10)
            tsp.text2speech("You are doing a Good Job!")
            flag = True
            if flag:
                try:
                    cr.robot_listen()
                    flag = False
                except:
                    pass 
            time.sleep(5)
                  
        elif "bye" in userResponse:
            tsp.text2speech("You did some amazing work today. Good bye! Let's meet again")
            break
        elif userResponse == "":
            continue
        elif ("brown fox") in userResponse or ("she sells") in userResponse or ("peter piper") in userResponse or ("cow") in userResponse:
            continue
        else :
            tsp.text2speech("i didn't quite catch that. Could you please repeat it again? Thank you!'")
            continue
        
        time.sleep(1)