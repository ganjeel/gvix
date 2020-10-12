import wikipedia

from resources.apps.speaker import speaker
from resources.apps.recognizer import recognizer

wikipedia.set_lang("es")

class wiki():
    def __init__(self):
        self.speaker = speaker()
        self.recognizer = recognizer()

    # función que ejecuta la busqueda en sí
    def wikisearch(self, what):
        self.speaker.say(str(wikipedia.summary(what, sentences = 1)))

    # genera una frase o palabra a partir de un array
    def phraser(self, query):
        phrase = ""
        if len(query) > 1:
            for words in query:
                phrase = "{} {}".format(phrase, words)
            return phrase
        else:
            return query[0]

    # genera una frase o palabra a partir de un array
    def phraser(self, query):
        phrase = ""
        if len(query) > 1:
            for words in query:
                phrase = "{} {}".format(phrase, words)
            return phrase
        else:
            return query[0]

    def wiki(self):
        self.speaker.say("Que deseas buscar en wikipedia?")
        # paso la respuesta por phraser y despues la envío a wikisearch
        try: 
            self.wikisearch(self.phraser(self.recognizer.hear()))
        except wikipedia.exceptions.PageError:
            self.speaker.say("Ese término no corresponde a una página de wikipedia.")