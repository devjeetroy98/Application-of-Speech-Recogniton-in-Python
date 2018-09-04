import speech_recognition as sr
import pyaudio
import time

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening...", end='')
    time.sleep(.3)
    print(".", end='')
    time.sleep(0.01)
    print(".")
    audio = r.listen(source)
    r.adjust_for_ambient_noise(source, duration=4)
    text = r.recognize_google(audio)

try:
    print(text)
except sr.RequestError:
    print("Google speech recognition could not get the audio!!")
except sr.UnknownValuerror:
    print("Could not fetch the results properly!!")