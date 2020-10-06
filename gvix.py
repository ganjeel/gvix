import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib



##################################################################
MASTER = "Gian"
wikipedia.set_lang("es")
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
mic = sr.Microphone()
r = sr.Recognizer()

#def wiki_search():

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



####################################################################
wikipedia.set_lang("es")
query = str(takeCommand(mic, r))
query = query.split()


for order, word in enumerate(query):
    query[order] = query[order].lower()


if "wikipedia" in query:
    speak("Que deseas buscar en wikipedia?")

    ans = str(takeCommand(mic, r))

    wiki_summary = wikipedia.summary(ans, sentences=2)

    speak("El resultado de la busqueda de {} es".format(ans))
    speak(str(wiki_summary))
elif "youtube" in query:
    try:
        #webbrowser.get("google-chrome").open_new("https://www.youtube.com")
        webbrowser.open("https://www.youtube.com")
    except webbrowser.Error:
        print("fFFFFFF")
