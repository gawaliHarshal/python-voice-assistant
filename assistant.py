import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime

# Initialize the voice engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speech speed
engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

def speak(text):
    """Speak the given text."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to user's voice and return as text."""
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        listener.adjust_for_ambient_noise(source)
        audio = listener.listen(source)

    try:
        command = listener.recognize_google(audio)
        command = command.lower()
        print("📢 You said:", command)
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Sorry, there's a network issue.")
        return ""

def run_assistant():
    while True:
        command = listen()

      


        if 'play' in command:
            song = command.replace('play', '').strip()
            speak(f"🎵 Playing {song}")
            pywhatkit.playonyt(song)

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"🕒 The current time is {time}")

        elif 'date' in command:
            date = datetime.datetime.now().strftime('%A, %B %d, %Y')
            speak(f"📅 Today's date is {date}")

        elif 'who is' in command:
            person = command.replace('who is', '').strip()
            try:
                info = wikipedia.summary(person, sentences=2)
                speak(info)
            except Exception as e:
                speak("Sorry, I couldn't find information on that.")

        elif 'stop' in command or 'exit' in command:
            speak("Goodbye!")
            break

        elif command:
            speak("Sorry, I didn't understand that command.")

        elif 'exit' in command or 'stop' in command or 'quit' in command:
         speak("Goodbye!")
         break


# Run it!
if __name__ == '__main__':
    speak("Hello! How can I help you today?")
    run_assistant()


# import datetime
# import pyttsx3
# import speech_recognition as sr

# # Initialize Text-to-Speech Engine
# engine = pyttsx3.init()
# engine.setProperty('rate', 150)
# engine.setProperty('volume', 1.0)

# def speak(text):
#     print(f"🗣️ Assistant: {text}")
#     engine.say(text)
#     engine.runAndWait()

# def listen():
#     recognizer = sr.Recognizer()
#     recognizer.energy_threshold = 300  # Optional: faster, less calibration
#     recognizer.dynamic_energy_threshold = False

#     with sr.Microphone() as source:
#         print("🎙️ Listening...")
#         try:
#             audio = recognizer.listen(source, timeout=5)
#             command = recognizer.recognize_google(audio).lower()
#             print(f"📢 You said: {command}")
#             return command
#         except sr.WaitTimeoutError:
#             speak("I didn't hear anything.")
#         except sr.UnknownValueError:
#             speak("Sorry, I didn't understand that.")
#         except sr.RequestError:
#             speak("Network error.")
#     return ""

# def run_assistant():
#     import pywhatkit
#     import wikipedia

#     name = "Harshal"

#     while True:
#         command = listen()

#         if not command:
#             continue

#         if 'play' in command:
#             song = command.replace('play', '').strip()
#             speak(f"🎵 Playing {song}")
#             pywhatkit.playonyt(song)

#         elif 'time' in command:
#             time = datetime.datetime.now().strftime('%I:%M %p')
#             speak(f"The time is {time}")

#         elif 'date' in command:
#             date = datetime.datetime.now().strftime('%A, %B %d, %Y')
#             speak(f"Today is {date}")

#         elif 'who is' in command:
#             person = command.replace('who is', '').strip()
#             try:
#                 info = wikipedia.summary(person, sentences=2)
#                 speak(info)
#             except:
#                 speak("Sorry, I couldn't find that person.")

#         elif 'what is my name' in command or 'do you know my name' in command:
#             speak(f"Yes, your name is {name}!")

#         elif 'stop' in command or 'exit' in command or 'quit' in command:
#             speak("Goodbye!")
#             break

#         else:
#             speak("Sorry, I didn't understand that.")

# # Entry point
# if __name__ == '__main__':
#     speak("Hello! How can I help you today?")
#     run_assistant()
