# =====================================
# negotiation_analytics.py
# =====================================

class NegotiationAnalytics:

    def __init__(self, memory, state_machine):

        self.memory = memory
        self.state_machine = state_machine

    def get_total_rounds(self):

        transcript = self.memory.get_transcript()

        user_messages = [

            x for x in transcript

            if x["speaker"] == "USER"

        ]

        return len(user_messages)

    def get_outcome(self):

        return self.state_machine.get_state()

    def get_negotiation_score(self):

        transcript = self.memory.get_transcript()

        total_messages = len(transcript)

        score = min(

            100,

            40 + (total_messages * 5)

        )

        return score

    def get_duration_seconds(self):

        transcript = self.memory.get_transcript()

        if len(transcript) < 2:

            return 0

        start_time = transcript[0]["timestamp"]

        end_time = transcript[-1]["timestamp"]

        duration = end_time - start_time

        return duration.total_seconds()

    def get_efficiency(self):

        rounds = self.get_total_rounds()

        if rounds <= 3:

            return "Excellent"

        elif rounds <= 6:

            return "Good"

        elif rounds <= 10:

            return "Average"

        return "Poor"

    def get_quality(self):

        score = self.get_negotiation_score()

        if score >= 90:

            return "Excellent"

        elif score >= 75:

            return "Good"

        elif score >= 60:

            return "Average"

        return "Poor"

    def get_summary(self):

        return {

            "total_rounds":
            self.get_total_rounds(),

            "outcome":
            self.get_outcome(),

            "duration_seconds":
            self.get_duration_seconds(),

            "negotiation_score":
            self.get_negotiation_score(),

            "efficiency":
            self.get_efficiency(),

            "quality":
            self.get_quality()

        }

