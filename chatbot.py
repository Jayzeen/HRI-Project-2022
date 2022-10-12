import speech_recognition as sr
import text_to_speech as tsp
import speech_to_text as stt
import whisperApi as whisper
import wikipedia
import pyjokes
import time
import pvporcupine as pv
import pyaudio
import struct
import winsound
import winaudio


def ConversationFlow():
    while True:
        userResponse = stt.takeCommand()
        
        if "hello" in userResponse:
            tsp.text2speech("Hello friend")
        elif "tell me a joke" in userResponse:
            joke = pyjokes.get_joke()
            tsp.text2speech(joke)
        elif "tell me about" in userResponse:
            summaryRes = wikipedia.summary(userResponse, 1)
            tsp.text2speech(summaryRes)
        elif "bye" in userResponse:
            tsp.text2speech("Bye bye now.")
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
                ConversationFlow()
                time.sleep(1)
                endSound()
                print("*********** Chat bot is sleeping*************")
    finally:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if pa is not None:
            pa.terminate()
        

    
main()