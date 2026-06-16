# =====================================
# intent_classifier.py
# =====================================

import re


class IntentClassifier:

    def __init__(self):

        self.intent_patterns = {

            "GREETING": [
                r"\bhi\b",
                r"\bhello\b",
                r"\bhey\b",
                r"\bgood morning\b",
                r"\bgood evening\b"
            ],

            "ACCEPT": [
                r"\bi accept\b",
                r"\baccept\b",
                r"\bdeal\b",
                r"\bagreed\b",
                r"\baccepted\b",
                r"\bfinal deal\b",
                r"\blets do it\b"
            ],

            "REJECT": [
                r"\breject\b",
                r"\bnot interested\b",
                r"\bdecline\b",
                r"\bno deal\b"
            ],

            "EXIT": [
                r"\bbye\b",
                r"\bquit\b",
                r"\bexit\b",
                r"\bleave\b"
            ]
        }

    def classify(self, text):

        text = text.lower().strip()

        # OFFER detection

        if re.search(r"\d+", text):
            return "OFFER"

        # Other intents

        for intent, patterns in self.intent_patterns.items():

            for pattern in patterns:

                if re.search(pattern, text):
                    return intent

        return "UNKNOWN"