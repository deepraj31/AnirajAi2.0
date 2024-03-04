import pyttsx3
import speech_recognition as sr


def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 174)
    # print(voices)
    engine.say(text)
    engine.runAndWait()
    
def take_commmand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening..')
        r.pause_threshold  = 1
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source, 10, 6)

    try:
        print('Recognizing..')
        query = r.recognize_google(audio, language='en-in')
        print(f'User Said: {query}')
    except Exception as e:
        return ''
    
    return query.lower()


text = take_commmand()

speak(text)