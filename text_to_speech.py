import pyttsx3


def text2speech(text):
    # initialize Text-to-speech engine
    engine = pyttsx3.init()

    # Get available voices
    voices = engine.getProperty("voices")

    # Set voice to what we want
    engine.setProperty("voice", voices[2].id)
    engine.setProperty("rate", 150)

    # play the speech
    engine.say(text)


    engine.runAndWait()
    

    