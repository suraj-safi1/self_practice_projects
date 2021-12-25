# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 04:58:59 2021

@author: safis
"""
import pyttsx3
import speech_recognition as sr
import datetime



engine= pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
         speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak('Good Afternoon!')
    else:
        speak("Good Evening!")

    speak("I am jarvis sir. Please tell me how i help you sir")
def takeCommand():
    r = sr.Recogniser()
    with sr.Microphone() as source:
        print('Listing.....')
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio ,Language='en-in')
        print(f"user said: {query}\n")
    
    except Exception as e:
        #print(e)
        print("say that again please....")
        return "none"
    return query
if __name__ == "_main_":
    wishMe()
    takeCommand()