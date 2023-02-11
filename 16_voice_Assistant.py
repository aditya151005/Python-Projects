# voice se commannd dena and convert into text 
import pyttsx3 #text to speech
import speech_recognition as sr #
import webbrowser
import datetime # run time me time
import pyjokes #One line jokes for programmers (jokes as a service)
def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
        try:
            print("recognizing...")
            data=recognizer.recognize_google(audio,language= 'en-US')
            return data
        except sr.UnknownValueError :
            print(" Not Understanding ")
def speechtx(x):
    engine=pyttsx3.init()
    voices=engine.getProperty("voices")
    # engine.setProperty("voice",voices[0].id)#male voice
    engine.setProperty("voice",voices[1].id)#female voice
    rate=engine.getProperty('rate')
    engine.setProperty('rate',130) #default speed is also there
    engine.say(x)
    engine.runAndWait()    
# sptext()
# speechtx("Hello Everyone,My name is Aditya Ranjan")
if __name__=='__main__':
    if sptext().lower()=="hey aditya":
        print('test')
    else:
        print("thanks")
        
    