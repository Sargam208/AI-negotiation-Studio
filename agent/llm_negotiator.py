from agent.ai_response_generator import AIResponseGenerator


class LLMNegotiator:

    def __init__(
        self,
        role,
        goal,
        constraints,
        personality,
        memory
    ):

        self.role = role
        self.goal = goal
        self.constraints = constraints
        self.personality = personality
        self.memory = memory

        self.ai = AIResponseGenerator()

    def respond(
        self,
        user_message
    ):

        transcript = self.memory.get_transcript()

        scenario = f"""
You are a {self.role}.

Your objective:
{self.goal}

Constraints:
{self.constraints}

Negotiation Style:
{self.personality}

Important:

- Protect your interests.
- Do not immediately agree.
- Make counteroffers when appropriate.
- Ask strategic questions.
- Try to achieve your objective.
"""

        response = self.ai.generate(

            personality=self.personality,

            scenario=scenario,

            current_offer="Not Applicable",

            minimum_offer="Not Applicable",

            user_message=user_message,

            transcript=transcript

        )

        self.memory.add_message(
            "AGENT",
            response
        )

        return response