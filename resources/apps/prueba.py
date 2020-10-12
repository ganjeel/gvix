from beep import beep
from recognizer import recognizer
from speaker import speaker

recognizer = recognizer()
speaker = speaker()

query = recognizer.hear()
speaker.say(query)



