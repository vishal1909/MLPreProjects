#!/usr/bin/python3
"""
import speech_recognition as sr

r=sr.Recognizer()
with sr.Microphone() as source:
	print("Speak")
	audio=r.listen(source)
try:
	print("you said " +r.recognize_google(audio))
except sr.UnknownValueError:
	print("Could not understand audio")
except sr.RequestError as e:
	print("Could not request results; {0}".format(e))
"""



#!/usr/bin/python3

import speech_recognition as sr

r=sr.Recognizer()
with sr.Microphone() as source:
	print("speak")
	audio=r.listen(source,timeout=1,phrase_time_limit=5)

try:
     print("You said   " + r.recognize_google(audio))
except sr.UnknownValueError:
     print("could not understand audio")
except sr.RequestError as e:
     print("cpuld not request results;{0}".format(e))
