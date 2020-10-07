import speech_recognition
import winsound
import os

# Iniciar micrófono y intérprete para reconocimiento de voz
mic = speech_recognition.Microphone()
recognizer = speech_recognition.Recognizer()

def hear():
    query = []
    with mic as source:
        for i in range(2):
            winsound.PlaySound(os.getcwd() + "\\resources\\sounds\\CLICK7C.wav", winsound.SND_FILENAME)        audio = recognizer.listen(source)
    try:
        audio2text = str(recognizer.recognize_google(audio, language="es-ES")).lower()
        for order, word in enumerate(audio2text.split()):
            query.append(word.lower())
        return query

    except speech_recognition.UnknownValueError:
        speak("No te entendí, por favor, repíteme")
        return "None"