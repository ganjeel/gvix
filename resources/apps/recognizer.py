import speech_recognition

from resources.apps.speaker import speaker
from resources.apps.beep import beep

class recognizer(object):

    def __init__(self):
        # instancia de speaker
        self.__speaker = speaker()
        # instancias para micrófono y reconocedor
        self.__mic = speech_recognition.Microphone()
        self.__recognizer = speech_recognition.Recognizer()

    def hear(self):    
        query = []
        with self.__mic as source:
            for i in range(2):
                beep()
            audio = self.__recognizer.listen(source)
        try:
            audio2text = str(self.__recognizer.recognize_google(audio, language="es-ES")).lower()
            print(audio2text)
            for order, word in enumerate(audio2text.split()):
                query.append(word.lower())
            return query
        
        except speech_recognition.UnknownValueError:
            self.__speaker.say("No te entendí, por favor, repíteme")
            return "None"