from .core import SmartCore
from .audio import AudioEngine

class Brain:
    def __init__(self):
        # النواة الأساسية
        self.core = SmartCore()
        
        # محرك الصوت
        self.audio = AudioEngine()
        
        # ذاكرة قصيرة المدى
        self.short_memory = []

    def process(self):
        """
        الاستماع → تحليل الكلام → توليد الرد → نطق الرد
        """
        # 1. الاستماع
        user_text = self.audio.hear()
        
        if not user_text or len(user_text.strip()) == 0:
            self.audio.speak("هل يمكنك إعادة ما قلت؟")
            return

        # حفظ في الذاكرة القصيرة
        self.short_memory.append(user_text)
        if len(self.short_memory) > 10:
            self.short_memory.pop(0)

        # 2. تحليل الكلام عبر النواة
        response = self.core.generate_response(user_text)

        # 3. التكلم
        self.audio.speak(response)

    def teach(self, content: str):
        """
        تعليم جديد للنظام — يضاف للنواة ويتعلم منه
        """
        self.core.learn(content)

    def emotional_mode(self, mood: str):
        """
        تغيير نبرة وشخصية المساعد
        """
        self.core.set_mood(mood)
        self.audio.speak(f"حسناً، سأكون {mood} من الآن.")
