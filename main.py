import pyttsx3 
import pyaudio
import datetime 
import speech_recognition as sr
import wikipedia
import webbrowser
import pyautogui
import os
from PyDictionary import PyDictionary as Diction
import keyboard
from keyboard import press_and_release
import pygame
import pyjokes
from time import sleep

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 160)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")
        print("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")
        print("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")
        print("Good Evening Sir!")


    pygame.mixer.init()
    pygame.mixer.music.load('snapvideo.io_JARVIS TIKTOK PC SOUND FREE HIGH QUALITY  AC_DC WINDOWS STARTUP SOUND.mp3')
    pygame.mixer.music.play() 

    import time
    time.sleep(17)

    speak("I am Jarvis, Your personal AI, how may I help you?")
    print("I am J.A.R.V.I.S, Your personal AI, how may I help you?")


def takecommand():


    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:

        print("Say that again please")
        return "None"

    return query

def Dict():
    speak("Activated Dictionary")
    speak("Tell me The problem")
    probl = takecommand()
    
    if 'meaning' in probl:
        probl = probl.replace("what is the","")
        probl = probl.replace("jarvis","")
        probl = probl.replace("meaning of","")
        result = Diction.meaning(probl)
        speak(f"The meaning for {probl} is {result}")
        print(result)

def speedtest():
    import speedtest
    speak("Checking speed....")
    speed  = speedtest.Speedtest()
    downloading = speed.download()
    correctDown = int(downloading/800000)
    uploading = speed.upload()
    correctUpload = int(uploading/800000)

    if 'uploading' in query:
        speak(f"The uploading speed is {correctUpload} mbp s")

    elif 'downloading' in query:
        speak(f"The downloading speed is {correctDown} mbp s")
    
    else:
        speak(f"The downloading is {correctDown} mbp s and the uploading speed is {correctUpload} mbp s")
        print(f"The downloading is {correctDown} mbp s and the uploading speed is {correctUpload} mbp s")


def playcommand():
    
    try:
        
        os.system('TASKILL /F /im spotify.exe')
    
    except Exception as e:
        print(e)
    
    codePath = "C:\\Users\\anshu\\Desktop\\Spotify.lnk"
    os.startfile(codePath)

    speak("Ok Sir")


def SpotifyAuto():
    speak("Whats your command sir?")
    comm = takecommand()

    if 'pause' in comm:
        keyboard.press('space bar')

    elif 'resume' in comm:
        keyboard.press('space bar')
    
    elif 'next' in comm:
        keyboard.press_and_release('ctrl + right arrow')

    elif 'previous' in comm:
        keyboard.press_and_release('ctrl + left arrow')
    
    elif 'seek forward' in comm:
        keyboard.press_and_release('0xA0 + right arrow')

    elif 'seek backward' in comm:
        keyboard.press_and_release('0xA0 + left arrow')

    elif 'volume up' in comm:
        keyboard.press_and_release('ctrl + up arrow')

    elif 'volume down' in comm:
        keyboard.press_and_release('ctrl + down arrow')
    
    speak("Done Sir")

def bye():        
        hour = int(datetime.datetime.now().hour)
        if hour>=8 and hour<11:
            speak("Bye sir! enjoy your breakfast")

        elif hour>=13 and hour<15:
            speak("Bye sir! enjoy your lunch")

        elif hour>=20 and hour<23:
            speak("Bye sir! enjoy your dinner")
        
        else:
            speak("Bye sir! Have a nice day")

if __name__ == "__main__":
    wishMe()
    while True: 
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
            speak("opening youtube")

        elif 'google search' in query:
            import wikipedia as googleScrap
            query = query.replace("jarvis", "")
            query = query.replace("google search", "")
            query = query.replace("google", "")
            string =  query.split()
            search = ""
            for i in string:
                search += i

                search += "+"

            webbrowser.open(f"https://www.google.com/search?q={search}&oq={search}&aqs=chrome..69i57j0i512l9.4267j0j1&sourceid=chrome&ie=UTF-8&safe=active")
            speak("This is what I found on the web, sir")

        elif 'open edge' in query or 'open browser' in query:
            codePath = "C:\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Edge.lnk"
            os.startfile(codePath)
            speak("opening edge")
        
        elif 'open discord' in query:
            file = "C:\\Users\\anshu\\Desktop\\Discord.lnk"
            os.startfile(file)
            speak("opening discord")
        
        elif 'open music' in query or 'open apple music' in query:
            codePath = "C:\\Users\\anshu\\Desktop\\Apple Music.lnk"
            os.startfile(codePath)
            speak("opening apple music sir")
        
        elif 'hello' in query or 'hey' in query:
            speak("Hello sir! may I help you with something")
        
        elif 'favourite song' in query:
            speak("")
        
        elif 'who are you' in query:
            speak("Hi i am Jarvis Aditya Thukral's personal AI")
        
        elif 'how are you' in query:
            speak("Fine sir and you?")

        elif 'thank you' in query or 'thanks' in query:
            speak("my pleasure sir")

        elif 'how you doing' in query:
            speak("Fine sir, may I help you with something?")

        elif 'what is your name' in query:
            speak("I am jarvis an AI")

        elif 'my name' in query:
            speak("Your name is Aditya Thukral and your the creator of this AI")

        elif 'dictionary' in query:
            Dict()
        
        elif 'pause' in query:
            keyboard.press('space bar')

        elif 'resume' in query:
            keyboard.press('space bar')
        
        elif 'next' in query:
            keyboard.press_and_release('ctrl + right arrow')

        elif 'previous' in query:
            keyboard.press_and_release('ctrl + left arrow')
        
        elif 'seek forward' in query:
            keyboard.press_and_release('shift + right arrow')

        elif 'seek backward' in query:
            keyboard.press_and_release('shift + left arrow')

        elif 'volume up' in query:
            keyboard.press_and_release('ctrl + up arrow')

        elif 'volume down' in query:
            keyboard.press_and_release('ctrl + down arrow')
            
        elif 'spotify' in query:
            SpotifyAuto()

        elif 'youtube search' in query:
            speak("Ok Sir , This is what is found for your search!")
            query = query.replace("jarvis","")
            query = query.replace("youtube search" ,"")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            speak("Done sir ")
        
        elif 'downloading speed' in query:
            speedtest()

        elif 'uploading speed' in query:
            speedtest()
        
        elif 'internet speed' in query:
            speedtest()

        elif 'speed test' in query:
            speedtest()
        
        elif 'battery' in query or 'how much power left' in query or 'how much power we have' in query:
            import psutil
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"sir we have {percentage} percent battery in our system")
            print(f"{percentage} % battery")

        elif 'joke' in query:
            get = pyjokes.get_joke()
            speak(get)
            print(get)

        elif 'play' in query:
            playcommand()
            
            sleep(10)

            pyautogui.click(x=97, y=154)

            query = query.replace("jarvis","")
            query = query.replace("play" ,"")
            query = query.replace("Hi", "")

            keyboard.write(query)

            sleep(2)

            pyautogui.click(x=891, y=448)
            pyautogui.click(x=891, y=448)

            speak('Playing your Song sir')

        elif 'my songs' in query:
            playcommand()

            sleep(3)

            pyautogui.click(x=66, y=512)
            pyautogui.click(x=66, y=512)
 
        elif 'say' in query or 'se' in query:
            query = query.replace("jarvis","")
            query = query.replace("se" ,"")
            query = query.replace("say" ,"") 

        
            speak(query)
        
        elif 'baap' in query or 'who is your father' in query:
            speak('mera bap koi nahi hai, mai anaath, hu sadly')

        elif 'what is the time' in query or 'Jarvis time' in query or 'jarvis time bataao' in query or 'the time' in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            speak(f"Sir time is {hour} {min}")
            print(f"Time: {hour}:{min}")

        elif 'bye' in query or 'mar' in query or 'bai' in query:
            bye()
            exit() 
            