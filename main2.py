# import speech rexcognition to recognition of voice using microphone
import speech_recognition as sr
# import pyttsx  to covert text  or voice into speak
import pyttsx3
# import ewebbrowser to open the browser
import webbrowser
# to incluse usic file in our program
import musicLibrary
# import open Ai in out prohect using groq
from groq import Groq
# Both pyttsx3 and gTTS are popular Python text-to-speech libraries
# pyttsx3 is offline; gTTS is online.
from gtts import gTTS
import pygame
import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()
# Initialization
engine = pyttsx3.init()
# Api key to acess groq
API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=API_KEY)


    # setup to reply User cammand
def ask_groq(prompt):
    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are Jarvis, a smart voice assistant. Answer in short sentences."},
                {"role": "user", "content": prompt}
            ],
            model="llama-3.1-8b-instant"
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Groq API Error: {e}")
        return "I am having trouble connecting to AI."

def processcommand(c):
    # convert all string into lowercase
    c_lower = c.lower()
    # open google
    if "open google" in c_lower:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
        
        #open youtube
    elif "open youtube" in c_lower:
        speak("Opening Youtube")
        webbrowser.open("https://www.youtube.com")
        
        # open facebook
    elif "open facebook" in c_lower:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")
    
    
    elif c_lower.startswith("play"):
            song = c_lower.replace("play", "").strip()
            link=musicLibrary.music[song]
            webbrowser.open(link)  
    # --- NEW: News Reader Feature ---
    elif "news" in c_lower or "read news" in c_lower:
        get_news()        
    else:
        # Agar koi system command na ho, to Groq AI se puchain
        ai_reply = ask_groq(c)
        speak(ai_reply)
def old_speak(text):
    print(f"Jarvis: {text}")
    try:
        engine = pyttsx3.init('sapi5') # Windows speech driver
        engine.setProperty('rate', 170) # Speech speed
        engine.say(text)
        engine.runAndWait()
        engine.stop() # Clear speech queue
    except Exception as e:
        print(f"TTS Error: {e}")

def get_news():
    # Free working News API endpoint (Bina API key ke chalega)
    url = "https://saurav.tech/NewsAPI/top-headlines/category/general/us.json"
    speak("Fetching top headlines for you...")
    response = requests.get(url)
    data = response.json()
        
    if data.get("status") == "ok":
        articles = data.get("articles", [])[:3]  # Top 3 news headlines
            
        for i, article in enumerate(articles, 1):
            title = article.get("title")
            description = article.get("description")
                
            speak(f"News {i}: {title}")
            if description:
                speak(description)
    else:
        speak("Sorry, I could not fetch the news at the moment.")
def speak(text):
    print(f"Jarvis: {text}")
    file_name = "temp_voice.mp3"
        
        # 1. gTTS se text ko MP3 file mein save karein
    
    
    tts = gTTS(text=text, lang='en')
    tts.save(file_name)

        # 2. Pygame mixer initialize karke play karein
    pygame.mixer.init()
    pygame.mixer.music.load(file_name)
    pygame.mixer.music.play()

        # 3. Jab tak aawaz chal rahi hai, tab tak wait karein
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

        # 4. File free karein aur delete kar dein taake agli dafa masla na ho
    pygame.mixer.music.unload()
    os.remove(file_name)
                
# --- MAIN LOOP WITH WAKE WORD LOGIC ---
if __name__ == "__main__":
    speak("Initializing JArvis...")
    while True:
        r = sr.Recognizer()
        print("recognization")
        try:
            with sr.Microphone() as source:
                    # STAGE 1: Standby Mode (Listening for Wake Word)
                    print("listing")
                    audio = r.listen(source, timeout=5, phrase_time_limit=3)
                    word = r.recognize_google(audio)
                    if(word.lower()=="jarvis" or word.lower()=="hello"):
                        speak("Ya, I am listening...")
                        #listen for command
                        with sr.Microphone() as source:
                            print("jarvis activating.............")
                            speak("jarvis activating")
                            audio = r.listen(source, timeout=5, phrase_time_limit=3)
                            command= r.recognize_google(audio)
                            print(command)
                            processcommand(command)
        
        except Exception as e:
            print("Error, {0}".format(e))
            
            
        
       