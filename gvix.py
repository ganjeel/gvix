import speech_recognition
import pyttsx3
import wikipedia
import webbrowser
import os
import json
import time
import winsound

################################################################################

# Cargar data
cwd = os.getcwd()

with open(cwd + "\\settings\\url.json") as content:
    keywords = json.load(content)

claves = []
for clave, url in keywords.items():
    claves.append(clave)

print(claves)
# Cargar user confs
master = "fausto"
slave = "jaime"

# Iniciar micrófono y intérprete para reconocimiento de voz
mic = speech_recognition.Microphone()
recognizer = speech_recognition.Recognizer()

# Iniciar speaker
tts = pyttsx3.init()
# Conf de speaker (CARGAR EN DATA)
tts.setProperty("rate", 130) # velocidad
tts.setProperty("volume",1.0) # volumen entre 0 y 1

# Conf de wikipedia (CARGAR EN DATA)
wikipedia.set_lang("es")



################################################################################

def speak(what):
    tts.say(what)
    tts.runAndWait()

def hear():
    query = []
    with mic as source:
        winsound.PlaySound(cwd + "\\resources\\sounds\\CLICK7C.wav", winsound.SND_FILENAME)
        winsound.PlaySound(cwd + "\\resources\\sounds\\CLICK7C.wav", winsound.SND_FILENAME)
        audio = recognizer.listen(source)
    try:
        audio2text = str(recognizer.recognize_google(audio, language="es-ES")).lower()
        for order, word in enumerate(audio2text.split()):
            query.append(word.lower())
        return query

    except speech_recognition.UnknownValueError:
        speak("No te entendí, por favor, repíteme")
        return "None"

def wiki():
    speak("Que deseas buscar en wikipedia?")
    search = hear()
    try:
        if len(search) == 1:
            speak(str(wikipedia.summary(search, sentences = 1)))
        elif len(search) == 0:
            speak("Error")
        else:
            phrase = ""
            for words in search:
                phrase = "{} {}".format(phrase,words)
            print(phrase)
            speak(str(wikipedia.summary(search, sentences = 1)))
    except wikipedia.exceptions.DisambiguationError:
        speak("Error")

def browse(keywords, claves, query):
    check = False
    for clave in claves:
        if clave in query:
            check = True
            try:
                webbrowser.open(keywords[clave])
            except webbrowser.Error:
                speak("Error")

    if check == False:
        while check == False:
            speak("Qué página deseas abrir?")
            ans = hear()
            for keyword in ans:
                if keyword in claves:
                    try:
                        print(keywords[keyword])
                        webbrowser.open(keywords[keyword])
                        check = True
                    except webbrowser.Error:
                        speak("Error")
                        break

            if check == False:
                speak("No entendí la página, debería buscarla en google?")
                new_ans = hear()
                if "sí" in new_ans:
                    phrase = ""
                    for words in ans:
                        phrase = "{} {}".format(phrase, words)
                        print(phrase)
                    webbrowser.open("https://www.google.com/search?q={}".format(phrase))
                    check = True
                else:
                    speak("Quieres repetir la palabra?")
                    new_ans = hear()
                    if "sí" in new_ans:
                        pass
                    else:
                        break

def gsearh():
    speak("Que deseas buscar en google?")
    ans = hear()
    phrase = ""
    for words in ans:
        phrase = "{} {}".format(phrase, words)
        print(phrase)
    webbrowser.open("https://www.google.com/search?q={}".format(phrase))

################################################################################


while True:

    speak("Te escucho..")
    query = hear()
    print(query)

    if slave in query:
        # A FUTURO USAR UN DICCIONARIO
        # DE LISTAS DE PALABRAS CLAVES
        # PARA REFERIRNOS A FUNCIONES
        if "abrir" in query: 
            browse(keywords, claves, query)
        elif "wikipedia" in query:
            wiki()
        elif "google" in query:
            gsearh()
