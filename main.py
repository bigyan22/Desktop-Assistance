import pyttsx3
import os
import speech_recognition as sr
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Renognizing...')
        query = r.recognize_google(audio, language="en-NP")
        print(f"User said: {query}")
        return query.lower()
    except Exception as e:
        print('say that again please')
        return 'none'
print("Welcome to Desktop Assistance 'Bolt'!")

def greeting():
    hour = datetime.datetime.now().hour
    
    if hour > 0 and hour < 12:
        speak('Good Morning!')
    elif hour >= 12 and hour < 16:
        speak('Good Evening!')
    else:
        speak('Good Night!')
greeting()
speak("I am Desktop Assistance 'Bolt'! How can I help you today!")
while True:
    query = takecommands()
    if 'quit' in query:
        speak('Bye Bye friend!')
        quit()
    else:
        speak(query)
        