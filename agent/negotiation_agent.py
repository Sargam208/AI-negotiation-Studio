# =====================================
# negotiation_agent.py
# =====================================

from agent.memory import NegotiationMemory

from agent.state_machine import StateMachine

from agent.ai_response_generator import (
    AIResponseGenerator
)

from nlp.ai_intent_classifier import (
    AIIntentClassifier
)


class NegotiationAgent:

    def __init__(

        self,

        personality="STRATEGIST",

        scenario="General Negotiation"

    ):

        self.personality = personality

        self.scenario = scenario

        self.memory = NegotiationMemory()

        self.state_machine = StateMachine()

        self.ai = AIResponseGenerator()

        self.intent_classifier = (
            AIIntentClassifier()
        )

    # =====================================
    # MAIN RESPONSE FUNCTION
    # =====================================

    def respond(

        self,

        user_message

    ):

        # ---------------------------------
        # Store User Message
        # ---------------------------------

        self.memory.add_message(

            "USER",

            user_message

        )

        # ---------------------------------
        # Build Transcript
        # ---------------------------------

        transcript = []

        for item in self.memory.get_transcript():

            transcript.append(

                f"{item['speaker']}: "
                f"{item['message']}"

            )

        transcript_text = "\n".join(
            transcript
        )

        # ---------------------------------
        # AI Intent Classification
        # ---------------------------------

        intent = (

            self.intent_classifier
            .classify(

                user_message,

                transcript_text

            )

        )

        # ---------------------------------
        # ACCEPT DEAL
        # ---------------------------------

        if intent == "ACCEPT_DEAL":

            self.state_machine.transition(
                "ACCEPT"
            )

            response = (

                "🤝 Agreement confirmed. "
                "Looking forward to working together."

            )

            self.memory.add_message(

                "AGENT",

                response

            )

            return {

                "state": "DEAL",

                "response": response

            }

        # ---------------------------------
        # REJECT DEAL
        # ---------------------------------

        if intent == "REJECT_DEAL":

            self.state_machine.transition(
                "REJECT"
            )

            response = (

                "Understood. Thank you for "
                "the discussion."

            )

            self.memory.add_message(

                "AGENT",

                response

            )

            return {

                "state": "NO_DEAL",

                "response": response

            }

        # ---------------------------------
        # EXIT NEGOTIATION
        # ---------------------------------

        if intent == "EXIT":

            self.state_machine.transition(
                "REJECT"
            )

            response = (
                "Negotiation closed."
            )

            self.memory.add_message(

                "AGENT",

                response

            )

            return {

                "state": "NO_DEAL",

                "response": response

            }

        # ---------------------------------
        # CONTINUE NEGOTIATION
        # ---------------------------------

        response = self.ai.generate(

            personality=
            self.personality,

            scenario=
            self.scenario,

            current_offer=
            "Unknown",

            minimum_offer=
            "Unknown",

            user_message=
            user_message,

            transcript=
            transcript_text

        )

        self.memory.add_message(

            "AGENT",

            response

        )

        return {

            "state": "ACTIVE",

            "response": response

        }

