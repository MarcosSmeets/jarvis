import pyttsx3 
import speech_recognition as sr 
import datetime
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Lord of the Galaxy!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Lord of the Galaxy!")   

    else:
        speak("Good Evening Lord of the Galaxy!")  

    speak("How may i help you")
       

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        if 'youtube' in query:
            url = 'https://www.youtube.com.br'
            webbrowser.open(url)
            speak('Done Sir')

        elif 'google' in query:
            url = 'https://www.google.com.br'
            webbrowser.open(url)
            speak('Done Sir') 

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")    
            speak(f"Sir, the time is {strTime}")
        
        elif 'spotify' in query:
            url = 'https://open.spotify.com'
            webbrowser.open(url)


        elif 'Twitch' in query:
            url = 'https://www.twitch.tv'
            webbrowser.open(url)
            speak('Done Sir')
        
        elif 'thank you' in query:
            speak('You Welcome Sir.')
            
        

            

        
  
