import speech_recognition as sr
import pyttsx3
import os

start = pyttsx3.init()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("скажи что-нибудь")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)
        try:
            task = r.recognize_google(audio, language="ru-RU").lower()
            print(task)
        except:
            task = listen()
        return task
def request(task):
    if "блокнот" in task:
        text = "открываю ваш блокнот"
        start.say(text)
        start.runAndWait()
        os.system("notepad")
    elif "калькулятор" in task:
        text = "открываю ваш калькулятор"
        start.say(text)
        start.runAndWait()
        os.system("calc")
    elif "милашка" in task:
        text = "фаризашка ты милашка, нарисуйка ты кошечку"
        start.say(text)
        start.runAndWait()
        os.system("mspaint")
    elif "привет" in task:
        text = "hi"
        start.say(text)
        start.runAndWait()
        os.system("narrator")
while True:
    request(listen())
listen()
