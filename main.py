import pyttsx3
import os
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import nepali.datetime as nepali
import random
import pywhatkit
import requests
import time
import pyjokes
import psutil
import subprocess
from dotenv import load_dotenv
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

load_dotenv()
apikey = os.getenv('API_KEY')

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
    print(hour)
    if hour > 0 and hour < 12:
        speak('Good Morning!')
    elif hour >= 12 and hour < 19:
        speak('Good Evening!')
    else:
        speak('Good Night!')
greeting()
speak("I am Desktop Assistance 'Bolt'! How can I help you today!")

def check_weather(city):
    speak('Checking the weather...')
    weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={apikey}"
    )
    temp = weather_data.json()['main']['temp']
    feels_temp = weather_data.json()['main']['feels_like']
    temp_C = (temp - 32)*5/9
    feels_c = (feels_temp-32)*5/9
    time.sleep(1.5)
    speak(f"The temperature in {city} is: {round(temp_C,2)}°C and it's feels like {round(feels_c, 2)}°C.")

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
    elif 'the weather' in query:
        speak("Which city weather do you want to check?")
        city = takecommands().lower()
        check_weather(city)
    elif 'where we are' in query or 'check the location' in query:
        speak('Wait sir, let me check the location....')
        try:
            ip_address = requests.get('https://api.ipify.org').text
            url = "https://get.geojs.io/v1/ip/geo/"+ip_address+ '.json'
            requ = requests.get(url)
            response = requ.json()
            province = response['region']
            city = response['city']
            country = response['country']
            time.sleep(1.5)
            speak(f'Successfully found. You are in {city} city of {province}, in the country {country}.')
        except Exception as e:
            speak("Sorry sir. I am unable to find the location. Try again!")
    elif 'tell me a joke' in query or 'make me a laugh' in query:
        speak("Sure, Here's the joke.")
        joke = pyjokes.get_joke()
        speak(joke)
        print(joke)
    elif 'open notepad' in query:
        speak("Opening notepad..")
        os.system('start notepad')
    elif 'open calculator' in query:
        speak("Opening calculator...")
        os.system('calc')
    elif 'open vscode' in query or 'open vs code' in query:
        # os.system('start code')
        path = "C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        speak("Opening VS Code.")
        os.startfile(path)
    elif 'open cmd' in query or 'open command prompt' in query:
        speak("Opening Command Prompt")
        os.system('start cmd')
    elif 'check battery percentage' in query or 'check battery status' in query:
        battery = psutil.sensors_battery()
        if battery:
            percentage = battery.percent
            charging = battery.power_plugged
            status = 'chargin' if charging else 'not charging'
            speak(f"Battery is at {percentage}% and is currently {status}.")
        else:
            print("battery status could not be determined. Sorry!")
            
    elif 'close notepad' in query:
        speak("Closing Notepad...")
        os.system('taskkill /f /im notepad.exe')
    elif 'close calculator' in query:
        speak("Closing Calculator...")
        try:
            subprocess.run('taskkill /f /fi "WINDOWTITLE eq Calculator"', shell=True)
        except Exception as e:
            speak("Could not close Calculator. Please try again.")
    elif 'close cmd' in query or 'close command prompt' in query:
        speak('Closing command prompt..')
        os.system('taskkill /f /im cmd.exe')
