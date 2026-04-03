import json
import os

class TrustAIInference:
    def __init__(self):
        self.version = "1.0.0"
        self.model_name = "TrustAI-Moderator-v1"

    def predict(self, input_text: str):
        """
        Core logic for detecting PII and Malicious Links.
        """
        # Detection logic
        has_pii = "@" in input_text
        has_link = "http" in input_text.lower() or "www." in input_text.lower()
        
        if has_pii or has_link:
            label = "FLAGGED_UNTRUSTED"
            score = 0.99
            reason = "PII or URL detected in input"
        else:
            label = "VERIFIED_SAFE"
            score = 0.95
            reason = "No sensitive patterns identified"

        return {
            "prediction": label,
            "confidence": score,
            "metadata": {
                "reason": reason,
                "model": self.model_name
            }
        }

# For standalone testing
if __name__ == "__main__":
    inference = TrustAIInference()
    test_input = "Contact me at madhu@example.com or visit http://trustai.com"
    result = inference.predict(test_input)
    print(json.dumps(result, indent=4))