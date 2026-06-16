# =====================================
# memory.py
# =====================================

from datetime import datetime
import pandas as pd


class NegotiationMemory:

    def __init__(self):

        self.history = []

        self.transcript = []

        self.round_count = 0

    # ----------------------------------
    # Store negotiation round
    # ----------------------------------

    def add_round(

        self,
        intent,
        user_offer,
        agent_offer,
        state

    ):

        self.round_count += 1

        record = {

            "round": self.round_count,

            "intent": intent,

            "user_offer": user_offer,

            "agent_offer": agent_offer,

            "state": state,

            "timestamp": datetime.now()

        }

        self.history.append(record)

    # ----------------------------------
    # Store conversation transcript
    # ----------------------------------

    def add_message(

        self,
        speaker,
        message

    ):

        self.transcript.append({

            "speaker": speaker,

            "message": message,

            "timestamp": datetime.now()

        })

    # ----------------------------------
    # Return negotiation history
    # ----------------------------------

    def get_history(self):

        return self.history

    # ----------------------------------
    # Return transcript
    # ----------------------------------

    def get_transcript(self):

        return self.transcript

    # ----------------------------------
    # Export history to CSV
    # ----------------------------------

    def export_csv(

        self,
        filename="negotiation_log.csv"

    ):

        df = pd.DataFrame(

            self.history

        )

        df.to_csv(

            filename,

            index=False

        )

        return filename

    # ----------------------------------
    # Reset memory
    # ----------------------------------

    def reset(self):

        self.history = []

        self.transcript = []

        self.round_count = 0