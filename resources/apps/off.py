from resources.apps.speaker import speaker
from resources.apps.recognizer import recognizer

speaker = speaker()
recognizer = recognizer()

def off():
	query = recognizer()
	if "sí" in query:
		exit()
