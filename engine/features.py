from playsound import playsound
import eel


# Playing assistant been sound function
@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\beep.mp3"
    playsound(music_dir)