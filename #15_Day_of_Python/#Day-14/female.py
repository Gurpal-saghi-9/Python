import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to set the voice to female
def set_female_voice():
    voices = engine.getProperty('voices')
    for voice in voices:
        if "Zira" in voice.name:  # Replace "Zira" with the female voice name on your system
            engine.setProperty('voice', voice.id)
            print(f"Set to female voice: {voice.name}")
            return
    print("No female voice found.")

# Apply the female voice
set_female_voice()

# Function to speak the text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Example usage
if __name__ == "__main__":
    speak("Hello, I am your virtual assistant. How can I help you?")
