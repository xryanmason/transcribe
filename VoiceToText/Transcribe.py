# Transcribe Voicemail
# Ryan Mason
# 06/11/2018

import speech_recognition as sr

# Path to file
AUDIO_FILE = 'C:\\Users\\Ryan\\Downloads\\Voicemail.wav'

# Read audio source file
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)

# Transcribe using Google Speech Recognition
try:
    print(r.recognize_google(audio))
except sr.UnknownValueError:
    print("Unintelligible")
except sr.RequestError as e:
    print("Unable to reach Google Speech Recognition service".format(e))
