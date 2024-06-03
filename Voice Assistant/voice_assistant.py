import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and the TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()


def listen():
    """Listen for audio and convert it to text"""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        print("Could not request results; check your network connection.")
        return None


def respond(command):
    """Respond to the recognized command"""
    if command:
        command = command.lower()
        if "hello" in command or "hi" in command:
            speak("Hello! How can I assist you today?")
        elif "your name please" in command or "who are you" in command:
            speak("I am your personal assistant.")
        elif "time" in command:
            from datetime import datetime
            now = datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {now}")
        elif "exit" in command or "turn off" in command or "shut down" in command:
            speak("Thank you, Goodbye!")
            return False
        else:
            speak(command)
    return True


def main():
    speak("Hello! I am your personal assistant. How can I help you today?")
    while True:
        command = listen()
        if not respond(command):
            break


if __name__ == "__main__":
    main()
