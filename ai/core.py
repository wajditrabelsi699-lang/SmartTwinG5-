class SmartCore:
    def __init__(self):
        self.memory = {}
        self.skills = []

    def learn(self, key, value):
        self.memory[key] = value

    def recall(self, key):
        return self.memory.get(key, "No data found")

    def add_skill(self, func):
        self.skills.append(func)

    def run(self):
        print("SmartTwin Core Engine Activated")
