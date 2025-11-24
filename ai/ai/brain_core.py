from .language_core import LanguageCore

class BrainCore:
    def __init__(self):
        self.language = LanguageCore()
        self.memory = []
        self.modes = {
            "normal": "Standard response mode.",
            "father": "Protective, guiding tone.",
            "mother": "Warm, emotional tone.",
            "friend": "Friendly supportive tone.",
        }

    def think(self, text: str, mode: str = "normal") -> str:
        """Processes user input and generates a response."""
        if mode not in self.modes:
            mode = "normal"

        # Step 1: Analyze input
        analyzed = self.language.analyze(text)

        # Step 2: Translate if needed
        translated = self.language.translate(text)

        # Step 3: Generate response
        response = self.language.generate_response(translated, mode=mode)

        # Step 4: Save to memory
        self.memory.append({"input": text, "response": response})

        return response

    def get_memory(self):
        return self.memory
