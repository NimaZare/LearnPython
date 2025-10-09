import pyttsx3
import speech_recognition as sr
from speech_recognition.recognizers import google


class TTS_STT_Tools:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()

    @staticmethod
    def text_to_speech(text):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        print("\n==> Speaking...")
        engine.say(text)
        engine.runAndWait()
        engine.stop()
        print("\n==> Done speaking.")

    
    @staticmethod
    def speech_to_text():
        recognizer = sr.Recognizer()
        recognizer.energy_threshold = 300
        recognizer.dynamic_energy_threshold = True

        with sr.Microphone() as source:
            print("\n==> Please speak now...\n")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source)

        try:
            text = google.recognize_legacy(recognizer=recognizer, audio_data=audio, language='fa-IR')
            print("\n==> You said: " + text)
            return text
        except sr.UnknownValueError:
            print("\n==> Sorry, I could not understand your speech.")
        except sr.RequestError as e:
            print(f"\n==> Could not request results from the speech recognition service; {e}")

