import pyttsx3
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)

engine.say("Oi Eu Sou a Mila")
engine.runAndWait()