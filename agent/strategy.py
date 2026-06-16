# =====================================
# strategy.py
# =====================================

class NegotiationStrategy:

    def __init__(
        self,
        opening_offer=50000,
        minimum_price=45000,
        max_rounds=5,
        personality="NORMAL"
    ):

        self.opening_offer = opening_offer

        self.minimum_price = minimum_price

        self.max_rounds = max_rounds

        self.personality = personality.upper()

        # Personality-based concession rates

        if self.personality == "SOFT":

            self.concession_rate = 2000

        elif self.personality == "HARD":

            self.concession_rate = 500

        else:

            self.concession_rate = 1000

    # ----------------------------------
    # Generate Counter Offer
    # ----------------------------------
    def generate_counter_offer(self, round_count):

        counter_offer = (

            self.opening_offer
            - (round_count * self.concession_rate)

        )

        # Never go below minimum price

        counter_offer = max(

            counter_offer,
            self.minimum_price

        )

        return counter_offer

    # ----------------------------------
    # Main Strategy Logic
    # ----------------------------------
    def evaluate_offer(

        self,
        user_offer,
        round_count

    ):

        # Max rounds reached

        if round_count >= self.max_rounds:

            return {

                "action": "TERMINATE",

                "message":
                "Maximum negotiation rounds reached."

            }

        # User offer above minimum

        if user_offer >= self.minimum_price:

            # Flexible negotiator

            if user_offer >= (

                self.minimum_price
                + self.concession_rate

            ):

                return {

                    "action": "ACCEPT",

                    "final_price": user_offer

                }

            else:

                final_counter = min(

                    self.minimum_price
                    + self.concession_rate,

                    self.opening_offer

                )

                return {

                    "action": "COUNTER",

                    "counter_offer":
                    final_counter

                }

        # User offer below minimum

        counter_offer = self.generate_counter_offer(

            round_count

        )

        return {

            "action": "COUNTER",

            "counter_offer":
            counter_offer

        }