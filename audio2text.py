import speech_recognition as sr
import time
audiofile=("C:\\Users\\abc\\Desktop\\Sample.wav")
#use of audio file as source
r=sr.Recognizer()
with sr.AudioFile(audiofile) as source:
    print("Recognizing..",end='')
    time.sleep(.3)
    print(".",end='')
    time.sleep(0.01)
    print(".")
    audio=r.record(source)       #initialize the recognizer!
try:
    print("The lyrics is as follows>> "+r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google speech recognition could not get the audio!!")
except sr.RequestError:
    print("Could not fetch the results properly!!")