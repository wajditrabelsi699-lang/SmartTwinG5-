from transformers import pipeline

class LanguageCore:
    def __init__(self):
        # المحرك الأساسي للفهم
        self.analyzer = pipeline("sentiment-analysis")
        
        # محرك الترجمة
        self.translator = pipeline("translation", model="Helsinki-NLP/opus-mt-mul-en")

    def analyze(self, text):
        """تحليل مشاعر + تحليل نبرة الكلام"""
        try:
            result = self.analyzer(text)
            return result[0]
        except:
            return {"label": "neutral", "score": 0.0}

    def translate(self, text):
        """ترجمة النص من أي لغة إلى الإنجليزية"""
        try:
            translated = self.translator(text)
            return translated[0]["translation_text"]
        except:
            return text

    def generate_response(self, text, mode="normal"):
        """توليد الرد حسب المزاج المختار"""

        tones = {
            "normal": "I understand. Here is the answer:",
            "father": "Listen my child, here is my advice:",
            "mother": "My dear, let me comfort you:",
            "friend": "Bro! let me tell you:",
        }

        intro = tones.get(mode, tones["normal"])
        return f"{intro} {text}"
