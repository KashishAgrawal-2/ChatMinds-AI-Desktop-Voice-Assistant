import speech_recognition as sr
import os
import win32com.client
import webbrowser
import wikipedia
import openai
from config import apikey
import datetime
import random


chatStr = ""
# https://youtu.be/Z3ZAJoi4x6Q
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Harry: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    speaker.speak(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]


def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    # print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from ChatMinds"


speaker = win32com.client.Dispatch("SAPI.SpVoice")
while 1:
    print('Welcome to Chat Minds')
    speaker.speak("Chat Minds AI")
    print("Listening.....")
    query = takeCommand()
    sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
             ["google", "https://www.google.com"], ["spotify","https://open.spotify.com/"], ["moodle","http://moodle.mitsgwalior.in/login/?lang=en"] ]
    for site in sites:
         if f"Open {site[0]}".lower() in query.lower():
            speaker.speak(f"Opening {site[0]} sir...")
            webbrowser.open(site[1])
    if "Open Youtube".lower() in query.lower():
        speaker.Speak("opening youtube sir....")
        webbrowser.open("http://youtube.com")
    if "open music".lower() in query.lower():
        musicPath = "C:/Users/hp/Downloads/Chaleya - Jawan 128 Kbps.mp3"
        os.startfile(musicPath)
    if "wikipedia".lower() in query.lower():
        speaker.Speak(f"Searching Wikipedia sir...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speaker.Speak("According to Wikipedia")
        print(results)
        speaker.Speak(results)
    elif "the time" in query:
        musicPath = "/Users/harry/Downloads/downfall-21371.mp3"
        hour = datetime.datetime.now().strftime("%H")
        min = datetime.datetime.now().strftime("%M")
        speaker.speak(f"Sir time is {hour} bajke {min} minutes")

    elif "Using artificial intelligence".lower() in query.lower():
        ai(prompt=query)

    elif "ChatMinds Quit".lower() in query.lower():
        exit()

    elif "reset chat".lower() in query.lower():
        chatStr = ""

    else:
        print("Chatting...")
        chat(query)



