import pyttsx3

# Iniciar speaker
tts = pyttsx3.init()
# Conf de speaker (CARGAR EN DATA)
tts.setProperty("rate", 130) # velocidad
tts.setProperty("volume",1.0) # volumen entre 0 y 1

def speak(what):
    tts.say(what)
    tts.runAndWait()