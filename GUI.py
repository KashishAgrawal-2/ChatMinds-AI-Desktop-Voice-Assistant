import tkinter as Tk
from tkinter import *
from PIL import ImageTk,Image
import speech_recognition as sr
import os
import pyttsx3
import webbrowser
import wikipedia
import smtplib
import datetime


print("Initialising ChatMinds")
sir = "KASHISH"

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good Morning"+sir)
    elif hour>=12 and hour<18:
        speak("Good Afternoon"+sir)
    else:
        speak("Good Evening"+sir)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing.....")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from ChatMinds"
            query=None
            return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('agrawalkashish222004@gmail.com', '7987191611')
    server.sendmail('gauravsharma4865@gmail.com', to, content)
    server.close()
class Widget:
    def __init__(self):
       root = Tk()

       root.title('ChatMinds')
       root.geometry('1280x720')

       img = ImageTk.PhotoImage(Image.open(r"C:/Users/hp/Downloads/chatmind.png"))
       panel = Label(root, image=img)
       panel.pack(side='right', fill='both', expand='no')

       self.compText = StringVar()
       self.userText = StringVar()

       self.userText.set("Click Run ChatMinds to give Command")
       userFrame = LabelFrame(root, text="User", font=('Arial', 12,'bold'))
       userFrame.pack(fill='both', expand='yes')
       left = Message(userFrame, textvariable= self.userText, bg='dark slate Blue', fg='white')
       left.config(font=("Century Gothic", 24, 'bold'))
       left.pack(fill='both', expand='yes')

       compFrame = LabelFrame(root, text="ChatMinds", font=('Arial', 12, 'bold'))
       compFrame.pack(fill='both', expand='yes')
       left2 = Message(compFrame, textvariable= self.compText, bg='light grey', fg='black')
       left2.config(font=("Century Gothic", 24, 'bold'))
       left2.pack(fill='both', expand='yes')

       self.compText.set('Hello I am ChatMinds !!! What can I do for you ')

       btn = Button(root, text="Run ChatMinds", font=("Black ops one", 10,'bold'),bg="black",fg="white",command=self.clicked)
       btn.pack(fill='x', expand='no')
       btn2 = Button(root, text='Close !', font=("Black ops one", 10, 'bold'), bg="black", fg="white",command=root.destroy)
       btn2.pack(fill='x', expand='no')

       root.mainloop()

    def clicked(self):
        print("Working")
        query = takeCommand()
        self.userText.set('Listening.......')
        self.userText.set(query)
        query=query.lower()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                 ["google", "https://www.google.com"], ["spotify", "https://open.spotify.com/"],
                 ["moodle", "http://moodle.mitsgwalior.in/login/?lang=en"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query:
                speak(f"Opening {site[0]} mam...")
                webbrowser.open(site[1])


        if "play music".lower() in query:
            speak("playing music sir....")
            musicPath = "C:/Users/hp/Downloads/Chaleya - Jawan 128 Kbps.mp3"
            os.startfile(musicPath)
        elif "wikipedia".lower() in query:
            speak(f"Searching Wikipedia sir...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            self.userText.set(results)
            speak(results)
        elif "time".lower() in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            speak(f"Sir time is {hour} and {min} minutes")
        elif "thank you".lower() in query:
            speak("Always pleasure to always help you")
        elif "sorry".lower() in query:
            speak("Its ok")
        elif 'who are you'.lower() in query:
            speak("I am ChatMinds, Mam")
    
        elif 'kashish'.lower() in query:
            try:
                speak("What should I say Mam")
                content = takeCommand()
                to = "agrawalkashish222004@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry Sir, i am not able to send this email at a moment")


if __name__ == '__main__':
    speak('INITIALISING CHATMINDS')
    wishme()
    widget = Widget()
