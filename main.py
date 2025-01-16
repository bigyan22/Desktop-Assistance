import pyttsx3
import os
import speech_recognition as sr


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
print("Welcome to Desktop Assistance!")
speak("Welcome to Desktop Assistance!")
while True:
    query = takecommands()
    if 'quit' in query:
        speak('Quitting the process. Bye friend.')
        quit()
    else:
        speak(query)
