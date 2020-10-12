from resources.main import apps

gvix = apps()

gvix.say("Bienvenido {}, soy {}, su asistente virtual".format(gvix.master, gvix.slave))

gvix.say("Recuerde que debe esperar a escuchar el sonido:")

for i in range(2):
	gvix.beep()

gvix.say("para comenzar a hablar, señor")

while True

	query = gvix.hear()
	gvix.categorize(query)

	if gvix.slave in query:

		category = gvix.categorize(query)
		gvix.wakewords[category](query)