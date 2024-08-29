#import library
import speech_recognition as sr
#Initiаlize  reсоgnizer  сlаss  (fоr  reсоgnizing  the  sрeeсh)
r = sr.Recognizer()
# Reading Audio file as source
#  listening  the  аudiо  file  аnd  stоre  in  аudiо_text  vаriаble
with sr.AudioFile(r"C:\Users\sohad\OneDrive\Desktop\Python\BacBon\harvard.wav") as source:
    audio_text = r.listen(source)
#This line is to get the source file from google collab, if you're working on collab.
#with sr.AudioFile(r"/content/harvard (1).wav") as source:
        #audio_text = r.listen(source)
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    try:
        # using google speech recognition
        text = r.recognize_google(audio_text)
        print('Converting audio transcripts into text ...')
        print(text)
    except:
         print('Sorry.. run again...')




