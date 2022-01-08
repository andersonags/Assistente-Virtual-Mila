import speech_recognition as sr
import pyttsx3

audio = sr.Recognizer()
machine = pyttsx3.init()

def execute_comand():

    try:
        with sr.Microphone() as source:
            print('Ouvindo...')
            voz = audio.listen(source)
            comand = audio.recognize_google(voz, language='pt-br')
            comand = comand.lower()
            if 'mila' in comand:
                comand = comand.replace('mila', '')
                machine.say(comand)
                machine.runAndWait()

    except:
        print('Microfone não está ok!')

    return comand 
