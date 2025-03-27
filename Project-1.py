import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests


engine = pyttsx3.init()
newsAPI = "b6c6b68624a94c0d8651c45eb9b6b7a6"

def speak(text):
    engine.say(text)
    engine.runAndWait()


def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1] 
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "open news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey=b6c6b68624a94c0d8651c45eb9b6b7a6")
        if r.status_code == 200:
        # Parse the JSON response
            data = r.json()
        # Extract the articles
            articles = data.get('articles', [])
        # Speak the headlines
            for article in articles:
                speak(article['title'])
    


if __name__ == "__main__":
    speak("Initializing Gemini....")
    print("To initialize Gemini speak Hello")
    #Listen for the wake word Jarvis
    #obtain audio from the microphone.
    while True:
        r = sr.Recognizer()
        print("Recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout = 3,phrase_time_limit=3)
            word = r.recognize_google(audio)
            if word.lower() == "hello":
                speak("Ya")
                #Listen for command.
                with sr.Microphone() as source:
                    print("Gemini Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processcommand(command)
        

        except Exception as e:
            print("Error; {0}".format(e))
