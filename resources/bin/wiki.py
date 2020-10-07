import wikipedia

# Conf de wikipedia (CARGAR EN DATA)
wikipedia.set_lang("es")

def wiki(search):
    speak("Que deseas buscar en wikipedia?")
    search = hear()
    if len(search) == 1:
        speak(str(wikipedia.summary(search, sentences = 1)))
    elif len(search) == 0:
        speak("Error")
    else:
        phrase = ""
        for words in search:
            phrase = "{} {}".format(phrase,words)
        speak(str(wikipedia.summary(search, sentences = 1)))
