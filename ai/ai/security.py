import hashlib

class SecurityLayer:
    def __init__(self):
        self.locked = False

    def fingerprint(self, data: str):
        """بصمة رقمية لأي محاولة لفك النواة"""
        return hashlib.sha256(data.encode()).hexdigest()

    def intrusion_detect(self, attempt: str):
        """كشف محاولة لمس أو تفكيك"""
        fp = self.fingerprint(attempt)
        print("⚠️ Intrusion detected:", fp)
        return "BLOCKED"

    def burn_layer(self):
        """حماية ذاتية — تفعيل طبقة حرق وهمية تلف كل نسخة خارجية"""
        self.locked = True
        return "🔥 Core shield activated — unauthorized access destroyed"
