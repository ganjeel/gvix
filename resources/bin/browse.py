import webbrowser

from resourses.bin.speak import speak

def browse(keywords, claves, query):
    check = False
    for clave in claves:
        if clave in query:
            check = True
            try:
                webbrowser.open(keywords[clave])
            except webbrowser.Error:
                speak("Error")

    if check == False:
        while check == False:
            speak("Qué página deseas abrir?")
            ans = hear()
            for keyword in ans:
                if keyword in claves:
                    try:
                        print(keywords[keyword])
                        webbrowser.open(keywords[keyword])
                        check = True
                    except webbrowser.Error:
                        speak("Error")
                        break

            if check == False:
                speak("No entendí la página, debería buscarla en google?")
                new_ans = hear()
                if "sí" in new_ans:
                    phrase = ""
                    for words in ans:
                        phrase = "{} {}".format(phrase, words)
                        print(phrase)
                    webbrowser.open("https://www.google.com/search?q={}".format(phrase))
                    check = True
                else:
                    speak("Quieres repetir la palabra?")
                    new_ans = hear()
                    if "sí" in new_ans:
                        pass
                    else:
                        break
