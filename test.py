import speech_recognition as sr
import text_to_speech as tsp
import whisperApi as whisper
import wikipedia


init_rec = sr.Recognizer()
print("Let's speak!!")
with sr.Microphone() as source:
    audio_data = init_rec.record(source, duration=5)
    print("Recognizing your text.............")
    text = init_rec.recognize_google(audio_data)
    text = text.lower()
    print(text)
    print("--------------------------------")
    
    # if (text == "tell me a joke"):
    #     joke = pyjokes.get_joke()
    #     tsp.text2speech(joke)
    # info = wikipedia.summary(text, 1)
    
    # tsp.text2speech(info)
    # whisper.talkSarcastically(text)
    # print(response)