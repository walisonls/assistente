import voice_input
import voice_output

texto = voice_input.ouvir_microfone()

print("Você disse: " + texto)

if texto == "Olá":
    resposta = "Olá, Como o senhor está?"
else:
    resposta = "não entendi, pode repetir, por favor?"

print("MAQUINA: " + resposta)

voice_output.saida_audio_text(resposta)