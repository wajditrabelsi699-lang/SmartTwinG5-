import speech_recognition as sr
import pyttsx3

class AudioEngine:
    def __init__(self):
        # محرك السمع
        self.listener = sr.Recognizer()
        
        # محرك الكلام
        self.speaker = pyttsx3.init()
        
        # ضبط سرعة الصوت حتى يكون لطيف وثابت
        self.speaker.setProperty('rate', 160)
        self.speaker.setProperty('volume', 0.9)

    def hear(self):
        """
        الاستماع لصوت المستخدم وتحويله لنص
        """
        try:
            with sr.Microphone() as source:
                print("أنا أستمع إليك…")
                audio = self.listener.listen(source)
                
                # ترجمة الصوت إلى نص
                text = self.listener.recognize_google(audio, language="ar")
                return text

        except Exception as e:
            return "لم أستطع سماعك بوضوح."

    def speak(self, text: str):
        """
        التكلم والرد على المستخدم
        """
        try:
            self.speaker.say(text)
            self.speaker.runAndWait()
        except:
            print("خطأ في تشغيل الصوت")
