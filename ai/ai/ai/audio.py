import speech_recognition as sr
import pyttsx3

class AudioEngine:
    def __init__(self):
        self.listener = sr.Recognizer()
        self.speaker = pyttsx3.init()
        self.speaker.setProperty('rate', 160)

    def hear(self):
        """الاستماع لصوت المستخدم وتحويله لنص"""
        try:
            with sr.Microphone() as source:
                audio = self.listener.listen(source)
                text = self.listener.recognize_google(audio, language="ar")
                return text
        except:
            return "لم أسمعك جيداً."

    def speak(self, text: str):
        """التكلم والرد على المستخدم"""
        self.speaker.say(text)
        self.speaker.runAndWait()
