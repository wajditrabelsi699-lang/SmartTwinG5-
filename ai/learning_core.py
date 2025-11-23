import json
import os

class LearningCore:
    def __init__(self, storage_path="storage/knowledge.json"):
        self.storage_path = storage_path
        self.memory = {}
        
        # إنشاء مجلد التخزين إن لم يكن موجوداً
        os.makedirs(os.path.dirname(storage_path), exist_ok=True)

        # تحميل الذاكرة القديمة إن وجدت
        self._load_memory()

    def _load_memory(self):
        """تحميل بيانات التعلم من التخزين"""
        if os.path.exists(self.storage_path):
            try:
                with open(self.storage_path, "r", encoding="utf-8") as f:
                    self.memory = json.load(f)
            except:
                self.memory = {}
        else:
            self.memory = {}

    def _save_memory(self):
        """حفظ البيانات على الجهاز"""
        with open(self.storage_path, "w", encoding="utf-8") as f:
            json.dump(self.memory, f, ensure_ascii=False, indent=4)

    def learn(self, text: str):
        """
        التعلم من أي محتوى يقدمه المستخدم
        """
        if not text or len(text.strip()) == 0:
            return
        
        # حفظ النص في تصنيف بسيط حسب الكلمات
        for word in text.split():
            word = word.lower()
            if word not in self.memory:
                self.memory[word] = []
            if text not in self.memory[word]:
                self.memory[word].append(text)

        # حفظ التحديثات
        self._save_memory()

    def recall(self, keyword: str):
        """
        استرجاع المعرفة المتعلقة بكلمة معينة
        """
        keyword = keyword.lower()
        return self.memory.get(keyword, [])

    def search(self, query: str):
        """
        بحث ذكي داخلي في كل الذاكرة
        """
        results = []
        query = query.lower()
        
        for key, values in self.memory.items():
            if query in key:
                results.extend(values)

        return list(set(results))

    def deep_learn(self, text: str):
        """
        التعلم العميق: تحويل نص كبير إلى ذاكرة منظمة
        """
        for sentence in text.split("."):
            clean = sentence.strip()
            if len(clean) > 3:
                self.learn(clean)
