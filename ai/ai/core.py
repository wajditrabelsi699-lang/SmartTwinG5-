class SmartCore:
    def __init__(self):
        self.short_memory = []
        self.long_memory = {}
        self.skills = []

        self.modes = {
            "normal": "Standard mode",
            "father": "Protective guiding mode",
            "mother": "Emotional warm mode",
            "friend": "Friendly supportive mode",
        }

        self.current_mode = "normal"
        self.security_flag = False

    def learn(self, key, value):
        self.long_memory[key] = value

    def recall(self, key):
        return self.long_memory.get(key, "No data found")

    def save_short(self, text):
        self.short_memory.append(text)
        if len(self.short_memory) > 20:
            self.short_memory.pop(0)

    def add_skill(self, func):
        self.skills.append(func)

    def run_skills(self, input_text):
        output = input_text
        for skill in self.skills:
            output = skill(output)
        return output

    def detect_intrusion(self, text):
        bad = ["hack", "break", "inject", "root", "decode"]
        for word in bad:
            if word in text.lower():
                self.security_flag = True
                return True
        return False

    def protect(self):
        if self.security_flag:
            return "⚠️ Attempt blocked."
        return None

    def set_mode(self, mode):
        if mode in self.modes:
            self.current_mode = mode
        else:
            self.current_mode = "normal"

    def run(self):
        print("SmartTwin Core Engine Activated")
