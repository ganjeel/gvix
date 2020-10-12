from pynput.keyboard import Key, Controller
        	

def discord(query):
	# función que activa el bind ctrl + [key]
	def ctrl_hotkey(key):
		with keyboard.pressed(Key.ctrl):
			keyboard.press(key)
			keyboard.release(key)

	for word in query:
		if word == "micro":
			ctrl_hotkey("o")
       	elif word in ["auri", "audi", "auris", "audis"]:
        	ctrl_hotkey("p")
