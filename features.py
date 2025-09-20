import datetime
import webbrowser
import wikipedia
import pywhatkit
import keyboard   # For media keys
from utils import speak

# Optional: Volume control (Windows only)
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


def play_song(song):
    speak(f"Playing {song} on YouTube")
    pywhatkit.playonyt(song)


def tell_time():
    time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {time}")


def wiki_search(topic):
    try:
        info = wikipedia.summary(topic, sentences=2)
        speak(info)
    except:
        speak("Sorry, I couldn't find that on Wikipedia.")


def open_youtube():
    speak("Opening YouTube")
    webbrowser.open("https://www.youtube.com")


# ========== MEDIA CONTROL ==========
def media_control(command):
    """Control system media (play, pause, next, volume)"""
    if "pause" in command:
        keyboard.send("media play/pause")
        speak("Paused")

    elif "resume" in command or "play" in command:
        keyboard.send("media play/pause")
        speak("Resumed")

    elif "next" in command:
        keyboard.send("media next")
        speak("Skipped to next track")

    elif "previous" in command:
        keyboard.send("media previous")
        speak("Playing previous track")

    elif "volume up" in command:
        adjust_volume(0.1)  # Increase by 10%
        speak("Volume increased")

    elif "volume down" in command:
        adjust_volume(-0.1)  # Decrease by 10%
        speak("Volume decreased")


def adjust_volume(change):
    """Adjust system volume by percentage"""
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    current = volume.GetMasterVolumeLevelScalar()
    new_volume = min(max(current + change, 0.0), 1.0)
    volume.SetMasterVolumeLevelScalar(new_volume, None)
