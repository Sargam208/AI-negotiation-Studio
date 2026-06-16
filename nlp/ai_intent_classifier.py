
# =====================================
# ai_intent_classifier.py
# =====================================

import os

from groq import Groq

from dotenv import load_dotenv

load_dotenv()


class AIIntentClassifier:

    def __init__(self):

        self.client = Groq(

            api_key=os.getenv(
                "GROQ_API_KEY"
            )

        )

    def classify(

        self,

        message,

        transcript

    ):

        prompt = f"""
You are an intent classifier for an AI negotiation system.

Return ONLY ONE label from:

ACCEPT_DEAL
REJECT_DEAL
EXIT
CONTINUE

Rules:

- Greetings (hi, hello, hey) = CONTINUE
- Questions = CONTINUE
- Offers = CONTINUE
- Counteroffers = CONTINUE
- Negotiation discussion = CONTINUE

Only return ACCEPT_DEAL if the user is clearly finalizing the agreement.

Examples:

"hi" -> CONTINUE
"hello" -> CONTINUE
"yes" -> CONTINUE
"okay" -> CONTINUE
"sounds good" -> CONTINUE
"can you do 55?" -> CONTINUE

"i accept" -> ACCEPT_DEAL
"deal done" -> ACCEPT_DEAL
"agreement confirmed" -> ACCEPT_DEAL
"let's finalize" -> ACCEPT_DEAL

"no deal" -> REJECT_DEAL
"i reject this" -> REJECT_DEAL

"bye" -> EXIT
"quit" -> EXIT

Conversation History:

{transcript}

Latest User Message:

{message}

Return ONLY the label.
"""

        response = self.client.chat.completions.create(

            model="llama-3.1-8b-instant",

            messages=[

                {
                    "role": "user",
                    "content": prompt
                }

            ],

            temperature=0

        )

        raw = (

            response
            .choices[0]
            .message
            .content
            .strip()
            .upper()

        )

        print("INTENT DEBUG:", raw)

        # Safe Parsing

        if "ACCEPT_DEAL" in raw:

            return "ACCEPT_DEAL"

        if "REJECT_DEAL" in raw:

            return "REJECT_DEAL"

        if raw == "EXIT":

            return "EXIT"

        return "CONTINUE"

