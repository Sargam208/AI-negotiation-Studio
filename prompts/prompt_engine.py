# =====================================
# prompt_engine.py
# =====================================

from prompts.response_templates import RESPONSE_TEMPLATES


class PromptEngine:

    def __init__(self, personality="STRATEGIST"):

        self.personality = personality.upper()

        if self.personality not in RESPONSE_TEMPLATES:

            self.personality = "STRATEGIST"

    # ----------------------------------
    # Generate Response
    # ----------------------------------

    def generate(

        self,
        action,
        price=None

    ):

        template = RESPONSE_TEMPLATES[
            self.personality
        ].get(action)

        if template is None:

            return "Response unavailable."

        if "{price}" in template:

            return template.format(

                price=price

            )

        return template