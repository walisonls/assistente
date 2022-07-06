import pyttsx3

def saida_audio_text(texto):
    engine = pyttsx3.init()

    """ RATE"""
    rate = engine.getProperty('rate')  # getting details of current speaking rate
    engine.setProperty('rate', 190)  # setting up new voice rate
    """VOLUME"""
    volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
    engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1
    """VOICE"""
    voices = engine.getProperty('voices')  # getting details of current voice
    # engine.setProperty('voice', voices[1].id)  #changing index, changes voices. 1 for female
    engine.setProperty('voice', voices[0].id)  # changing index, changes voices. 0 for male

    engine.say(texto)
    engine.runAndWait()