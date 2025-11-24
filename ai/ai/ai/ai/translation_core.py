
import random

class TranslationCore:
    def __init__(self):
        # اللغات المدعومة
        self.languages = ["ar", "en", "fr", "es"]
        
        self.simple_dictionary = {
            "hello": "مرحبا",
            "thanks": "شكرا",
            "love": "حب",
            "friend": "صديق",
            "yes": "نعم",
            "no": "لا",
        }

    def detect_language(self, text: str) -> str:
        arabic_chars = any("\u0600" <= c <= "\u06FF" for c in text)
        if arabic_chars:
            return "ar"
        return "en"  # افتراضي

    def translate_word(self, word: str) -> str:
        return self.simple_dictionary.get(word.lower(), word)

    def translate_sentence(self, text: str) -> str:
        words = text.split()
        translated = [self.translate_word(w) for w in words]
        return " ".join(translated)

    def smart_translate(self, text: str, target_lang: str):
        source = self.detect_language(text)

        if source == target_lang:
            return text

        if target_lang == "ar":
            return self.translate_sentence(text)

        # ترجمة بسيطة عكسية للغات الأخرى
        reversed_dict = {v: k for k, v in self.simple_dictionary.items()}

        words = text.split()
        translated = [reversed_dict.get(w.lower(), w) for w in words]

        return " ".join(translated)

    def random_style(self, text):
        styles = [
            f"🔸 ترجمة أدبية: {text}",
            f"🔹 ترجمة مبسطة: {text}",
            f"✨ ترجمة فصيحة: {text}",
        ]
        return random.choice(styles)
