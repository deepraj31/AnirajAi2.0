import pyttsx3
import speech_recognition as sr
import eel
import time



def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 174)
    # print(voices)
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()


   
def take_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening..')
        eel.DisplayMessage('Listening.....')
        r.pause_threshold  = 1
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source, 10, 6)

    try:
        print('Recognizing..')
        eel.DisplayMessage('Recognizing.....')
        query = r.recognize_google(audio, language='en-in')
        print(f'User Said: {query}')
        eel.DisplayMessage(query)
       
        # speak(query)
        
    except Exception as e:
        return ''
    
    return query.lower()

@eel.expose
def allCommands():
    try:
            
        query = take_command()
        # print(query)

        if "open" in query :
            from engine.features import openCommand
            openCommand(query)

        elif "on youtube":
            from engine.features import PlayYoutube
            PlayYoutube(query)

        else:
            print("not run")
    except:
        speak("I didn't get that, please say again..")

    eel.ShowHood()