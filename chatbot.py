import text_to_speech as tsp
import speech_to_text as stt
import whisperApi as whisper
import startTrainingPlan as tp
from multiprocessing import Process

import wikipedia
import pyjokes
import time
import pvporcupine as pv
import pyaudio
import struct
import winsound
import winaudio
import keyboard
import sys


def ConversationFlow():
    while True:
        userResponse = stt.takeCommand()
        
        if "hello" in userResponse:
            tsp.text2speech("Hello friend")
            
        elif "tell me a joke" in userResponse:
            try:
                joke = pyjokes.get_joke()
                tsp.text2speech(joke)
            except:
                tsp.text2speech("Sorry i am not in the mood for jokes. Please try again later when i am in the mood")
                
        elif "tell me about" in userResponse:
            try:
                summaryRes = wikipedia.summary(userResponse, 1)
                tsp.text2speech("okay here is the summary.")
                tsp.text2speech(summaryRes)
            except:
                tsp.text2speech("Sorry i was unable to find anything about your topic")
                
        elif ("do a lesson") in userResponse or ("training plan") in userResponse:
            try:
                tsp.text2speech("Great!! We are going to do a lesson.")
                tp.StartTrainingPlan()
            except:
                tsp.text2speech("Sorry, i didn't quite catch that. Could you please repeat it again? Thank you!")
                
        elif "bye" in userResponse:
            tsp.text2speech("I'm going to miss you.Bye bye now.")
            break  
        
        elif "stop" in userResponse:
            tsp.text2speech("Good bye! Let's meet again")
            break
        
        elif userResponse == "":
            continue
        
        else :
            whisper.talkCasual(userResponse)
        
        time.sleep(1)

def wakeUpSound():
    windows_sounds = winaudio.get_windows_sounds(ext_filter=('wav', ))
    sound_path = windows_sounds.get('Windows Logon') 
    winaudio.play_wave_sound(sound_path, winaudio.SND_SYNC)  # Wait Until Finish  
    
def endSound():
    winsound.Beep(600, 300)
    winsound.Beep(600, 400)
    winsound.Beep(400, 500)      

def main():
    porcupine = None
    pa = None
    audio_stream = None
    print("Listening in background \n")
    
    try:
        porcupine = pv.create(keywords=["bumblebee", "jarvis"])
        pa = pyaudio.PyAudio()
        audio_stream = pa.open(
            rate = porcupine.sample_rate,
            channels = 1,
            format = pyaudio.paInt16,
            input = True,
            frames_per_buffer = porcupine.frame_length
        )
        
        while True:
            pcm = audio_stream.read(porcupine.frame_length)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
            
            keyword_index = porcupine.process(pcm)
            if keyword_index >= 0:
                wakeUpSound()
                print("*********** Chat bot is waking up*************")
                print("===========================================")
                tsp.text2speech("You woke me up. I guess you are in the mood for a lesson then. Let's go")
                ConversationFlow()
                time.sleep(2)
                endSound()
                print("*********** Chat bot is sleeping*************")
                print("Listening in background \n")
    finally:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if pa is not None:
            pa.terminate()


def interrupt(p1):
    while True:
        if keyboard.is_pressed("q"):
            time.sleep(5)
            tsp.text2speech("It looks like you are in a hurry. Let's continue this later.")
            tsp.text2speech("Have a nice day!")
            print("User interrupted the program. Killing all processes")
            p1.terminate()
            endSound()
            sys.exit()
        

if __name__=='__main__':    
    p1 = Process(target=main)
    p1.start()

    p2= Process(target=interrupt(p1))