import pyttsx3
import datetime
import speech_recognition as sr
import os
import cv2
from requests import get
import wikipedia
import webbrowser
import sys
import pyjokes
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)

# Text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# To wish the user
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")

    elif hour>=12 and hour<18:
        speak("Good afternoon!")

    else:
        speak("Good evening!")

    speak("I am jarvis, how may i help you?")

# To convert voice into text
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        #print(e)
        speak("Say that again please....")
        print("Say that again please....")
        return "None"
    return query

# for news updates
def news():
    main_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=2fab8f7184e14631bfaf5c03ac855c5e'
    main_page = requests.get(main_url).json()
    # print(main_page)
    articles = main_page["articles"]
    # print(articles)
    head = []
    day = ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")

if __name__ == "__main__":
    wishMe()
    #while True:
    if 1:

        query = takeCommand().lower()

        # logic building for tasks

        if "open notepad" in query:
            apath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(apath)

        elif "close notepad" in query:
            speak("closing notepad")
            os.system("taskkill /f /im notepad.exe")  # works only for while loop

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")
            
        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open google" in query:
            speak("what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif "switch off" in query:
            speak("switching off.")
            sys.exit()        # jarvis turns off and will not take anymore commands from user.

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke(language='en')  # no need to add any parameters for english language.
            speak(joke)

        elif "news" in query:
            speak("fetching the latest news...")
            news()
            




