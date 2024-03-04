from playsound import playsound
import eel
from engine.config import ASSISTANT_NAME
from engine.command import *
import os
import pywhatkit as kit
import re


# Playing assistant been sound function
@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\beep.mp3"
    playsound(music_dir)


def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    # app_name = query.strip()

    if query != "":

        speak(f"Opening {query} ")
        os.system(f'start {query}')


    else:
        speak("Not found")



def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing "+search_term+" on YouTube")
    kit.playonyt(search_term)


def extract_yt_term(command):
    # Define a regular expression pattern to capture the song name
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    # Use re.search to find the match in the command
    match = re.search(pattern, command, re.IGNORECASE)
    # If a match is found, return the extracted song name; otherwise, return None
    return match.group(1) if match else None