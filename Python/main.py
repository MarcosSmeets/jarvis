from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import smtplib

def talkToMe(audio):
    print(audio)
    tts = gTTS(text = audio, lang='en')
    tts.save('audio.mp3')
    os.system('npg123 audio.mp3')

#listem for commands

def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('I am ready for your next command')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listem(source)

    try:
        command = r.recognize_google(audio)
        print('you said: ' + command + '/n')
    
    #loop back to listen to commands

    except sr.UnknowValeuError:
        assistant(myCommand())
    
    return command

#if statements for executing commands

def assistant(command):
    if 'open Reddit python' in command:
        chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        url = 'https://www.reddit.com/r/python'
        webbrowser.get(chrome_path).open(url)
    if 'what\'s up' in command:
        talkToMe('Chillin bro')
    if 'drop my needle' in command:
        chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        url = "https://open.spotify.com"
        webbrowser.get(chrome_path).open(url)

        
    
    
talkToMe('I am ready for your new command')

while True:
    assistant(myCommand())