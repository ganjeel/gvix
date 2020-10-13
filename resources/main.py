from fuzzywuzzy import process
from resources.apps.off import off
from resources.apps.beep import beep
from resources.apps.loader import loader
from resources.apps.recognizer import recognizer
from resources.apps.speaker import speaker
from resources.apps.browser import browser
from resources.apps.gsearch import gsearch
from resources.apps.launcher import launcher
from resources.apps.wiki import wiki
# from resources.apps.discord import discord

class apps():
	# instancias y parámetros
	def __init__(self):
		self.master = loader()["settings"]["master"]
		self.slave = loader()["settings"]["slave"]

		self.recognizer = recognizer()
		self.speaker = speaker()
		self.browser = browser()
		self.gsearch = gsearch()
		self.launcher = launcher()
		self.wiki = wiki()

		self.wakewords = {
			"abrir" : self.browse,
			"buscar en google" : self.search,
			"iniciar" : self.launch,
			"wikipedia" : self.wikipedia,
			"salir" : self.off
		}

		self.categories = []
		for words in self.wakewords:
			self.categories.append(words)

	def off(self):
		pass

	# escucha y devulve una lista de palabras que escuchó
	def hear(self):
		query = self.recognizer.hear()
		return query

	def categorize(self, query):
		phrase = ""
		for words in query:		
			phrase += words
			phrase += " "
		category = process.extractOne(phrase, self.categories)
		return category[0]

	# tts [what]
	def say(self, what):
		self.speaker.say(what)

	# hacer sonido
	def beep(self, query):
		beep()

	# abrir en el navegador
	def browse(self, query):
		self.browser.browse(query)

	# buscar en google
	def search(self, query):
		self.gsearch.searcher(query)

	# iniciar programa
	def launch(self, query):
		self.launcher.launch(query)

	def wikipedia(self, query):
		self.wiki.wiki()

	# toggles discord
	# def discord(self, query):
	# 	discord(query)