#BIBLIOTECAS:
#pip install SpeechRecognition
#pip install pyttsx3
#pip install PyAudio (em versões abaixo de 3.6)
#(em versões acima de 3.6 use isto para instalar o PyAudio)
#pip install pipwin
#pipwin install pyaudio

import speech_recognition as sr
import pyttsx3

audio = sr.Recognizer()
maquina = pyttsx3.init()


try:
    with sr.Microphone() as source:
        print('ouvindo...')
        voz = audio.listen(source)
        comando = audio.recognize_google(voz, language='pt-BR')
        comando = comando.lower()
        if 'mizaki' in comando:
            print(comando)
            maquina.say(comando)
            maquina.runAndWait()
except:
    print('Microfone não esta OK')
