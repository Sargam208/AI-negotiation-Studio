# =====================================
# state_machine.py
# =====================================

class StateMachine:

    def __init__(self):

        self.current_state = "ACTIVE"

        self.history = ["ACTIVE"]

    def transition(self, intent):

        # Terminal protection
        if self.current_state in ["DEAL", "NO_DEAL"]:

            return self.current_state

        # State transitions
        if intent == "ACCEPT":

            self.current_state = "DEAL"

        elif intent == "REJECT":

            self.current_state = "NO_DEAL"

        else:

            self.current_state = "ACTIVE"

        self.history.append(self.current_state)

        return self.current_state

    def get_state(self):

        return self.current_state

    def get_history(self):

        return self.history