import speech_recognition as sr
import pyttsx3
from datetime import datetime

engine = pyttsx3.init()
recognizer = sr.Recognizer()


def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio)
            print("You:", command)
            return command.lower()

        except sr.UnknownValueError:
            return ""

        except sr.RequestError:
            speak("Speech recognition service is unavailable.")
            return ""

        except sr.WaitTimeoutError:
            return ""


def main():
    speak("Hello! I am Jarvis. How can I help you?")

    while True:
        command = listen()

        if "hello" in command or "hi" in command:
            speak("Hello! Nice to meet you.")

        elif "time" in command:
            current_time = datetime.now().strftime("%I:%M %p")
            speak(f"The time is {current_time}")

        elif "date" in command:
            today = datetime.now().strftime("%d %B %Y")
            speak(f"Today's date is {today}")

        elif "your name" in command:
            speak("My name is Jarvis.")

        elif "stop" in command or "exit" in command:
            speak("Goodbye!")
            break

        elif command:
            speak("Sorry, I don't understand that command.")


if __name__ == "__main__":
    main()