import speech_recognition as sr

# Cria um Reconhecedor
r = sr.Recognizer()

# Abrir o Microfone para captura
with sr.Microphone() as source:
    print('Ouvindo..')
while True:
    audio = r.listen(source) # Define Microfone como fonte de áudio

    print(r.recognizer_google(audio, language='pt-br'))