import os

from dotenv import load_dotenv
from nlp.groq_engine import GroqEngine

load_dotenv()


class AIResponseGenerator:

    def __init__(self):

        self.engine = GroqEngine(
            os.getenv("GROQ_API_KEY")
        )

    def generate(
        self,
        personality,
        scenario,
        current_offer,
        minimum_offer,
        user_message,
        transcript
    ):

        return self.engine.generate_response(

            personality=personality,

            scenario=scenario,

            current_offer=current_offer,

            minimum_offer=minimum_offer,

            user_message=user_message,

            transcript=transcript

        )