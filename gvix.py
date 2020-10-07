import speech_recognition
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import json
from gtts import gTTS as speak

################################################################################



mic = speech_recognition.Microphone()
recognizer = speech_recognition.Recognizer()


wikipedia.set_lang("es")
cwd = os.getcwd()

################################################################################

def load_data(where):
    with open(where) as content:
        return json.load(content)

def takeCommand(mic, recognizer):
    with mic as source:
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio, language="es-ES")
    except Exception:
        return None

def wiki(search):
    return str(wikipedia.summary(search, sentences = 1))
    
def browse(keyword, keywords):
    try:
        webbrowser.open(keywords[keyword])
    except webbrowser.Error:
        return False

################################################################################

keywords = load_data("settings/url.json")

query = str(takeCommand(mic, recognizer))
query = query.split()

for order, word in enumerate(query):
    query[order] = query[order].lower()


if "wikipedia" in query:
    speak("Que deseas buscar en wikipedia?")

    ans = str(takeCommand(mic, recognizer))

    wiki_summary = wiki(ans)

    speak("El resultado de la busqueda de {} es".format(ans))
    speak(str(wiki_summary))

if "abrir" or "navegador" or "chrome" in query:
    speak("Que página deseas abrir?")

    ans = str(takeCommand(mic, recognizer))

    browse(ans, keywords)
