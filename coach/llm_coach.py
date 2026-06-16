from agent.ai_response_generator import AIResponseGenerator


class LLMCoach:

    def __init__(self):

        self.ai = AIResponseGenerator()

    def generate_feedback(

        self,

        transcript,

        scenario

    ):

        conversation = "\n".join(

            [

                f"{msg['speaker']}: {msg['message']}"

                for msg in transcript

            ]

        )

        prompt = f"""
You are an expert negotiation coach.

Analyze this negotiation.

Provide:

1. Strength
2. Weakness
3. One actionable suggestion

Rules:

- Maximum 60 words
- Be specific
- Do not repeat the conversation
- Focus on negotiation quality

Conversation:

{conversation}
"""

        return self.ai.generate(

            personality="COACH",

            scenario=prompt,

            current_offer="N/A",

            minimum_offer="N/A",

            user_message="Analyze this negotiation.",

            transcript=[]

        )