import pyttsx3
import control_robot as cr

# ************* FUNCTIONS TO CONVERT TEXT TO SPEECH *************
def text2speech(text):
    # initialize Text-to-speech engine
    engine = pyttsx3.init()

    # Get available voices
    voices = engine.getProperty("voices")

    # Set voice to what we want
    engine.setProperty("voice", voices[3].id)
    engine.setProperty("rate", 150)

    # play the speech
    engine.say(text)

    engine.runAndWait()
    
    # Robot interaction
    flag = True
    if flag:
        try:
            cr.robot_listen()
            flag = False
        except:
            pass
    

def text2speech2(text):
    # initialize Text-to-speech engine
    engine = pyttsx3.init()

    # Get available voices
    voices = engine.getProperty("voices")
    # voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_LINDA_11.0"

    # Set voice to what we want
    engine.setProperty("voice", voices[3].id)
    engine.setProperty("rate", 150)

    # play the speech
    engine.say(text)

    engine.runAndWait()
    
    # Robot interaction
    # flag = True
    # if flag:
    #     try:
    #         cr.robot_listen()
    #         flag = False
    #     except:
    #         pass
    
    