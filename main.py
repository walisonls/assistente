import speech_recognition as sr

def ouvir_microfone():
    microfone = sr.Recognizer()

    with sr.Microphone() as source:
        # Chama um algoritimo de redução de ruidos
        microfone.adjust_for_ambient_noise(source)
        # Aviso para o usuario falar
        print("Ouvindo...")
        # Armazenar audio em uma variavel
        audio = microfone.listen(source)
    try:
        # Aplica um padrão de linguagem a variavel com a menssagem
        frase = microfone.recognize_google(audio, language='pt-BR')
        # Retorna a frase pronunciada
        print("Você disse: " + frase)
    except sr.UnknownValueError:
        print("Problema encontrado")

    return frase

ouvir_microfone()
