import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
from gtts import gTTS
import pygame
import os

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# API key for News API
newsapi = "<Your NewsAPI Key Here>"

# Function to speak text using pyttsx3
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to fetch and process AI response (using OpenAI or similar API)
def ai_process(command):
    # Mock AI response for demonstration purposes
    response = f"You said: {command}. This feature can be expanded with AI integration."
    return response

# Function to process commands
def process_command(command):
    command = command.lower()
    
    if "open google" in command:
        webbrowser.open("https://google.com")
        speak("Opening Google")
    elif "open facebook" in command:
        webbrowser.open("https://facebook.com")
        speak("Opening Facebook")
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")
    elif "open linkedin" in command:
        webbrowser.open("https://linkedin.com")
        speak("Opening LinkedIn")
    elif "news" in command:
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
            if r.status_code == 200:
                articles = r.json().get('articles', [])
                for article in articles[:5]:  # Limit to top 5 headlines
                    speak(article['title'])
            else:
                speak("I couldn't fetch the news right now.")
        except Exception as e:
            speak("An error occurred while fetching the news.")
            print(e)
    else:
        # Use AI to handle the request
        output = ai_process(command)
        speak(output)

# Main function to initialize Jarvis
if __name__ == "__main__":
    recognizer = sr.Recognizer()
    speak("Initializing Jarvis...")

    while True:
        try:
            print("Listening for wake word 'Jarvis'...")
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                wake_word = recognizer.recognize_google(audio)

                if wake_word.lower() == "jarvis":
                    speak("Yes, I am listening.")
                    print("Waiting for your command...")

                    # Listen for the actual command
                    with sr.Microphone() as source:
                        recognizer.adjust_for_ambient_noise(source)
                        audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
                        command = recognizer.recognize_google(audio)
                        print(f"Command: {command}")
                        process_command(command)

        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
