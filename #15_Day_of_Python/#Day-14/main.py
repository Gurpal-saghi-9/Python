import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "12d21c3618c748b29d7155e35479830a"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

     # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 

def aiProcess(command):
    client = OpenAI(api_key="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",
    )

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
    elif "song" in c.lower():
        webbrowser.open("https://youtu.be/0BP5umJLXEc?si=UYGl6wQfydzMlsxr")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

        # musicLibrary.music[song]
        # if song in musicLibrary.music:
        #     webbrowser.open(musicLibrary.music[song])
        # else:
        #     speak("Sorry, I don't have that song in my library.")

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey=12d21c3618c748b29d7155e35479830a")
        if r.status_code == 200:
            #press the JSON response
            data = r.json()

            #extract the articles
            articles = data.get("articles",[])

            #print the headlines
            for article in articles:
                speak(article["title"])

    else:
        #let openai to handle request
        output = aiProcess(c)
        speak(output)

if  __name__ == '__main__':
    speak("Initializing jarvis.....")
    while True:
        # Listen for the wake word "jarvis"
        r = sr.Recognizer()
        
        print("Recognizing...")
        # recognize speech using Google coco
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source)
            word = r.recognize_google(audio)
            if(word.lower() == "gurpal"):
                speak("yeah, guru")
                # Listen for the command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("jarvis error; {0}".format(e))