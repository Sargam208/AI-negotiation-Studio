from groq import Groq


class GroqEngine:

    def __init__(self, api_key):

        self.client = Groq(
            api_key=api_key
        )

    def generate_response(
        self,
        personality,
        scenario,
        current_offer,
        minimum_offer,
        user_message,
        transcript
    ):

        prompt = f"""
You are acting as:

{scenario}

Negotiator personality:
{personality}

Conversation History:
{transcript}

User:
{user_message}

Rules:

- Stay in character.
- You are negotiating, not chatting.
- Respond like a real human negotiator.
- Maximum 2 short sentences.
- Maximum 50 words.
- Never write long paragraphs.
- Never explain everything.
- Ask at most ONE question.
- Be concise and direct.
"""

        response = self.client.chat.completions.create(

    model="llama-3.3-70b-versatile",

    temperature=0.8,

    max_tokens=80,

    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

        return response.choices[0].message.content