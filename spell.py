import pyttsx3 # pip install pyttsx3
import speech_recognition as pr # pip install SpeechRecongnition
import vlc
import time
import vlc_ctrl
engine = pyttsx3.init()
rate = engine.getProperty('rate')                         
engine.setProperty('rate', 120)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(prad):
    engine.say(prad)
    engine.runAndWait()
def takeCommand():
    r = pr.Recognizer()  # initalising the recogniser
    with pr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1 # wait for one second and then listen the audio
        audio = r.listen(source) # source nothing but listening our microphone
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') # Recognize our voice
        # Requires an internet connection
        print(query)

    except Exception as e:
        print(e)
        speak("Say that thing again please...")
        return 'None'
    return query
s = takeCommand()

#ci = vlc.MediaPlayer("C:/Users/Sakthi/Downloads/Trolls World Tour (2020) [1080p] [WEBRip] [5.1] [YTS.MX]/troll_2.mp4")
#ci.play()
#time.sleep(7200)