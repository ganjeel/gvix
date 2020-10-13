from resources.main import apps

gvix = apps()

# gvix.say("Bienvenido {}, soy {}, su asistente virtual".format(gvix.master, gvix.slave))
# gvix.say("Recuerde que debe esperar a escuchar el sonido:")

# for i in range(2):
# 	gvix.beep()

# gvix.say("para comenzar a hablar, señor")

while True:
	print("..")
	query = gvix.hear()

	if gvix.slave in query:

		x = query.index(gvix.slave)

		query = query[x:]

		category = gvix.categorize(query)
		gvix.commands[category](query)