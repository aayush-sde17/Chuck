import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech
engine = pyttsx3.init()
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Change voice here

def speak(text):
    """Convert text to speech"""
    print("Chuck:", text)
    engine.say(text)
    engine.runAndWait()

def listen_command():
    """Listen and recognize speech"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn’t catch that.")
        return ""
    except sr.RequestError:
        speak("Speech service unavailable.")
        return ""
