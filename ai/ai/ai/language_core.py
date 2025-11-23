from langdetect import detect
from googletrans import Translator

class LanguageCore:
    def __init__(self):
        # المترجم
        self.translator = Translator()

        # اللغات المتاحة
        self.supported_languages = {
            "ar": "العربية",
            "en": "English",
            "fr": "Français",
            "zh-cn": "简体中文",
            "ja": "日本語",
            "es": "Español",
            "de": "Deutsch"
        }

    def detect_language(self, text: str):
        """
        تحديد لغة النص تلقائياً
        """
        try:
            lang = detect(text)
            return lang
        except:
            return "unknown"

    def translate(self, text: str, target_lang: str):
        """
        الترجمة بين أي لغتين
        """
        try:
            result = self.translator.translate(text, dest=target_lang)
            return result.text
        except:
            return "❌ فشل في الترجمة"

    def auto_translate_reply(self, user_text: str, reply_text: str):
        """
        النظام يرد بنفس لغة المستخدم تلقائياً
        """
        user_lang = self.detect_language(user_text)

        if user_lang == "unknown":
            return reply_text

        if user_lang not in self.supported_languages:
            return reply_text

        try:
            translated = self.translator.translate(reply_text, dest=user_lang)
            return translated.text
        except:
            return reply_text

    def simplify_for_children(self, text: str, target_lang: str = "ar"):
        """
        تبسيط الجمل للأطفال (لغة أسهل)
        """
        simple = (
            text.replace("ذلك يشير إلى", "يعني")
                .replace("على الأرجح", "يمكن")
                .replace("بشكل عام", "عادة")
                .replace("على سبيل المثال", "مثلاً")
                .replace("معلومات معقدة", "شيء صعب")
        )

        try:
            result = self.translator.translate(simple, dest=target_lang)
            return result.text
        except:
            return simple

    def correct_language(self, text: str):
        """
        تصحيح لغوي أساسي
        """
        # تصحيح بسيط: مسافات – تنقيط – أخطاء شائعة
        fixed = text.strip()
        fixed = fixed.replace("هاذا", "هذا")
        fixed = fixed.replace("ان", "أن ")
        fixed = fixed.replace("هده", "هذه")

        return fixed
