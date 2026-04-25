import pyttsx3
import speech_recognition as sr
import datetime
import requests
import time
from newsapi import NewsApiClient

engine = pyttsx3.init()
newsapi = NewsApiClient(api_key="YOUR_API_KEY")  # 🔴 Put your API key here

#SPEAK
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

#LISTEN
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        speak("Sorry, I didn't understand")
        return ""

#FEATURES

# Time
def tell_time():
    time_now = datetime.datetime.now().strftime("%H:%M")
    speak(f"The time is {time_now}")

#Weather
def get_weather():
    speak("Tell city name")
    city = listen()
    if city:
        data = requests.get(f"https://wttr.in/{city}?format=3").text
        speak(data)

#News
def get_news():
    speak("Fetching latest news")
    headlines = newsapi.get_top_headlines(country="in")

    for article in headlines["articles"][:3]:
        speak(article["title"])

#Reminder
def set_reminder():
    speak("What should I remind?")
    task = listen()

    speak("After how many seconds?")
    try:
        seconds = int(listen())
        speak(f"Reminder set for {seconds} seconds")
        time.sleep(seconds)
        speak(f"Reminder: {task}")
    except:
        speak("Invalid input")

#MAIN
def run_assistant():
    speak("Hello Asmita, assistant started")

    while True:
        command = listen()

        if "time" in command:
            tell_time()

        elif "weather" in command:
            get_weather()

        elif "news" in command:
            get_news()

        elif "reminder" in command:
            set_reminder()

        elif "hello" in command:
            speak("Hello!")

        elif "stop" in command or "exit" in command:
            speak("Goodbye!")
            break

#RUN
if __name__ == "__main__":
    run_assistant()
