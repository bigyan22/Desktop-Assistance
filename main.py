import pyttsx3
import os
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import nepali.datetime as nepali
import random
import pywhatkit

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
        print('Recognizing...')
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
    query = takecommands().lower()
    if 'quit' in query:
        speak('Thank you for using me. Bye Bye friend!')
        quit()
    elif 'open facebook' in query:
        speak('Opening facebook..')
        webbrowser.open('https://www.facebook.com')
    elif 'open instagram' in query:
        speak('Opening instagram..')
        webbrowser.open('https://www.instagram.com')
    elif 'open youtube' in query:
        speak('Opening youtube....')
        webbrowser.open('https://www.youtube.com')
    elif 'open google' in query:
        speak('Opening google...')
        webbrowser.open('https://www.google.com')
    elif 'how are you' in query:
        command = '''
        I am good!'''
        speak(command)
    elif 'who are you' in query:
        command = 'My name is Bolt and I am Desktop Assistance.'
        speak(command)
    elif 'wikipedia' in query:
        speak('Searching wikipedia...')
        query = query.replace('wikipedia', " ") # replace the wikipedia by space
        result = wikipedia.summary(query, sentences=5)
        print(result)
        
        speak(f"According to wikipedia, {result}.")
        
    elif 'the time' in query:
        hour = datetime.datetime.now().hour
        minutes = datetime.datetime.now().minute
        seconds = datetime.datetime.now().second
        
        speak(f"The time is {hour} hours, {minutes} minutes and {seconds} seconds.")
    elif 'the date' in query or "today's english date" in query:
        date = datetime.datetime.now().strftime("%Y: %B :%d")
        speak(f"Today's date is: {date} ")
    elif 'today nepali date' in query or "today's nepali date" in query:
        nepali_months = [
            "Baisakh", "Jestha", "Ashadh", "Shrawan", "Bhadra", "Ashwin",
            "Kartik", "Mangsir", "Poush", "Magh", "Falgun", "Chaitra"
        ]

        try:
            ad_date = datetime.datetime.now().date()
            
            bs_date = nepali.nepalidate.from_date(ad_date)
            
            speak(f"Today's Nepali date is: {bs_date.year}, {nepali_months[bs_date.month-1]}, {bs_date.day}")
        except ValueError as e:
            speak('Sorry, there occurs an issue. Please try again.')
    elif 'play music' in query:
        music_dir = "E:\\music\\songs"
        songs = os.listdir(music_dir)
        rd = random.choice(songs)
        os.startfile(os.path.join(music_dir, rd))
        speak('Playing Music..')
        quit()
    elif 'play song on youtube' in query:
        speak('Which song do you want to listen on YouTube?')
        song = takecommands()
        
        speak("Enjoy the music...")
        pywhatkit.playonyt(song)
        quit()
    elif "search on google" in query:
        speak('What do you want to search on google?')
        question = takecommands()
        pywhatkit.search(question)