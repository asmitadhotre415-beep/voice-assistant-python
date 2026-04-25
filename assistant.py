import pyttsx3
import datetime
import requests
import time

engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    return input("You: ").lower()

def tell_time():
    speak(datetime.datetime.now().strftime("%H:%M"))

def get_weather():
    city = input("Enter city: ")
    data = requests.get(f"https://wttr.in/{city}?format=3").text
    speak(data)

def set_reminder():
    task = input("Reminder: ")
    seconds = int(input("Time (sec): "))
    time.sleep(seconds)
    speak(f"Reminder: {task}")

def run():
    speak("Assistant started")

    while True:
        command = listen()

        if "time" in command:
            tell_time()

        elif "weather" in command:
            get_weather()

        elif "reminder" in command:
            set_reminder()

        elif "hello" in command:
            speak("Hello!")

        elif "stop" in command:
            speak("Goodbye")
            break

if __name__ == "__main__":
    run()
