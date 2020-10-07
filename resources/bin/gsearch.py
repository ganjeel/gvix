import webbrowser

def gsearh():
    speak("Que deseas buscar en google?")
    ans = hear()
    phrase = ""
    for words in ans:
        phrase = "{} {}".format(phrase, words)
        print(phrase)
    webbrowser.open("https://www.google.com/search?q={}".format(phrase))