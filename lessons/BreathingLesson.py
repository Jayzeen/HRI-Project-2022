import text_to_speech as tsp
import speech_to_text as stt
import time
import control_robot as cr


def BreathingExerciseLesson():
    
    tsp.text2speech("Hello hello. So let's start the guided breathing exercises")
    tsp.text2speech("Take a few minutes to get ready to start.")
    time.sleep(2)
    while True:
        userResponse = stt.takeCommand()
        
        if "start" in userResponse:
            tsp.text2speech2("Okay, this first exercise is called  diaphragmatic breathing or Abdominal breathing")
            tsp.text2speech2("This exercise help you to become calmer and more relaxed")
            time.sleep(4)
            
            tsp.text2speech2("First, Lie on your back on a flat surface or in bed, with your knees bent and your head supported.")
            tsp.text2speech2("You can use a pillow under your knees to support your legs.")
            time.sleep(3)
            tsp.text2speech("Okay! You are doing a Good Job!")
            time.sleep(5)
            
            tsp.text2speech2("Now, Place one hand on your upper chest and the other just below your rib cage. ")
            tsp.text2speech2("This will allow you to feel your diaphragm move as you breathe.")
            time.sleep(5)
            
            tsp.text2speech2("Breathe in slowly through your nose so that your stomach moves out, causing your hand to rise.")
            tsp.text2speech2("The hand on your chest should remain as still as possible.")
            time.sleep(3)
            tsp.text2speech("Okay! You are doing a Good Job!")
            time.sleep(5)
            
            tsp.text2speech2("Tighten your stomach muscles, so that your stomach moves in ")
            tsp.text2speech2("causing your hand to lower as you exhale through pursed lips")
            tsp.text2speech2("The hand on your upper chest should remain as still as possible.")
            time.sleep(5)
            
            tsp.text2speech("Okay! Good Job!")
            flag = True
            if flag:
                try:
                    cr.robot_listen()
                    flag = False
                except:
                    pass 
            tsp.text2speech("Now shall we move on to the next breathing exercise")
            
        elif "next" in userResponse:
            tsp.text2speech("Okay, This next exercise is a sitting exercise")
            tsp.text2speech("As you gain more practice, you can try this diaphragmatic breathing technique while sitting in a chair")
            tsp.text2speech("Take a few minutes to get ready to start.")
            time.sleep(4)
            
            tsp.text2speech2("First, Sit comfortably, with your knees bent and your shoulders, head and neck relaxed.")
            time.sleep(5)
            
            tsp.text2speech2("Next, Place one hand on your upper chest and the other just below your rib cage. ")
            tsp.text2speech2("This will allow you to feel your diaphragm move as you breathe.")
            time.sleep(3)
            tsp.text2speech("Okay! You are doing a Good Job!")
            time.sleep(5)
            
            tsp.text2speech2("Then, Breathe in slowly through your nose so that your stomach moves out against your hand.")
            tsp.text2speech2("The hand on your chest should remain as still as possible.")
            time.sleep(5)
            
            tsp.text2speech2("Now, Tighten your stomach muscles, so that your stomach moves back in, as you exhale through pursed lips.")
            tsp.text2speech2("The hand on your upper chest must remain as still as possible.")
            time.sleep(5)
            
            tsp.text2speech("Wow! Nice Job!")
            flag = True
            if flag:
                try:
                    cr.robot_listen()
                    flag = False
                except:
                    pass 
            tsp.text2speech("Now repeat the above process for a few minutes")
              
        elif "bye" in userResponse:
            tsp.text2speech("Good bye! Let's meet again")
            break
        elif userResponse == "":
            continue
        else :
            tsp.text2speech("i didn't quite catch that. Could you please repeat it again? Thank you!'")
            continue
        
        time.sleep(1)