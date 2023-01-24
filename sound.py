import pyttsx3

tts = pyttsx3.init()

text = input("Введите текст, который хотите чтобы он произносил: ")

voices = tts.getProperty('voices')

tts.setProperty('voices', 'ru')

for voice in voices:
	if voice.name == 'Aleksandr':
		tts.setProperty('voice', voice.id)

tts.say(text)

tts.runAndWait()