import speech_recognition as sr

# Cria um Reconhecedor
r = sr.recognizer()

# Abrir o Microfone para captura
with sr.Micriphone() as source:
    audio = r.listem(source) # Define Microfone como fonte de áudio
    print(r.recognizer_google(audio))