import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import json

################################################################################

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
mic = sr.Microphone()
recon = sr.Recognizer()
wikipedia.set_lang("es")
cwd = os.getcwd()

################################################################################

def takeCommand(mic, r):
    with mic as source:
        print("Contame bro..")
        audio = r.listen(source)
    try:
        print("Interpretando")
        query = r.recognize_google(audio, language="es-ES")
        print(f"Dijiste: {query} \n")
    except Exception:
        print("Repetimelo bro")
    return query

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wiki(search):
    return str(wikipedia.summary(search, sentences = 1))
    
def browse(keyword):
    keywords = json.load("{}/settings/url.json".format(cwd))

    try:
        webbrowser.open(keywords[keyword])
    except webbrowser.Error:
        return error

################################################################################

query = str(takeCommand(mic, recon))
query = query.split()

for order, word in enumerate(query):
    query[order] = query[order].lower()


if "wikipedia" in query:
    speak("Que deseas buscar en wikipedia?")

    ans = str(takeCommand(mic, recon))

    wiki_summary = wiki(ans)

    speak("El resultado de la busqueda de {} es".format(ans))
    speak(str(wiki_summary))

if "abrir" or "navegador" or "chrome" in query:
    speak("Que página deseas abrir?")

    ans = str(takeCommand(mic, recon))

    browse(ans)
