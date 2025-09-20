from utils import speak, listen_command
from ai_module import ai_response
import features
import face_module


def process_command(command):
    if "play" in command and "youtube" in command:
        song = command.replace("play", "").replace("youtube", "")
        features.play_song(song)

    elif "time" in command:
        features.tell_time()

    elif "wikipedia" in command:
        topic = command.replace("wikipedia", "")
        features.wiki_search(topic)

    elif "open youtube" in command:
        features.open_youtube()

    # 📞 Calls & SMS (Twilio)
    elif "call" in command:
        number = input("Enter phone number: ")
        features.make_call(number)

    elif "text" in command:
        number = input("Enter phone number: ")
        message = input("Enter your message: ")
        features.send_text(number, message)

    # 🎵 Media control
    elif ("pause" in command or "resume" in command or 
          "next" in command or "previous" in command):
        features.media_control(command)

    elif "volume up" in command or "volume down" in command:
        features.media_control(command)

    # ❌ Exit
    elif "stop" in command or "exit" in command or "quit" in command:
        speak("Goodbye! Chuck signing off.")
        exit()
        
    elif "scan face" in command or "facial recognition" in command:
        face_module.load_faces()
        face_module.recognize_face()

    # 🤖 AI chat fallback
    else:
        response = ai_response(command)
        speak(response)


if __name__ == "__main__":
    speak("Hello! I’m Chuck, your personal voice assistant. How can I help you?")
    while True:
        user_command = listen_command()
        if user_command:
            process_command(user_command)
