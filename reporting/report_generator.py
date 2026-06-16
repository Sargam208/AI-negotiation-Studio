# =====================================
# report_generator.py
# =====================================

from datetime import datetime

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


class ReportGenerator:

    def __init__(

        self,

        memory,

        scenario,

        personality,

        outcome,

        coach_feedback,

        analytics

    ):

        self.memory = memory

        self.scenario = scenario

        self.personality = personality

        self.outcome = outcome

        self.coach_feedback = coach_feedback

        self.analytics = analytics

    # =====================================
    # Generate PDF
    # =====================================

    def generate_pdf(

        self,

        filename="Negotiation_Report.pdf"

    ):

        doc = SimpleDocTemplate(
            filename
        )

        styles = getSampleStyleSheet()

        content = []

        summary = (
            self.analytics.get_summary()
        )

        # =====================================
        # Title
        # =====================================

        content.append(

            Paragraph(

                "AI Negotiation Studio",

                styles["Title"]

            )

        )

        content.append(

            Paragraph(

                "Negotiation Analysis Report",

                styles["Heading2"]

            )

        )

        content.append(
            Spacer(1, 20)
        )

        # =====================================
        # Report Summary
        # =====================================

        timestamp = datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )

        content.append(

            Paragraph(

                "Report Summary",

                styles["Heading2"]

            )

        )

        content.append(
            Spacer(1, 10)
        )

        content.append(

            Paragraph(

                f"<b>Generated:</b> {timestamp}",

                styles["BodyText"]

            )

        )

        content.append(

            Paragraph(

                f"<b>Scenario:</b> {self.scenario}",

                styles["BodyText"]

            )

        )

        content.append(

            Paragraph(

                f"<b>Persona:</b> {self.personality}",

                styles["BodyText"]

            )

        )

        content.append(

            Paragraph(

                f"<b>Outcome:</b> {self.outcome}",

                styles["BodyText"]

            )

        )

        content.append(
            Spacer(1, 20)
        )

        # =====================================
        # Analytics
        # =====================================

        content.append(

            Paragraph(

                "Negotiation Analytics",

                styles["Heading2"]

            )

        )

        content.append(
            Spacer(1, 10)
        )

        content.append(

            Paragraph(

                f"<b>Total Rounds:</b> "
                f"{summary['total_rounds']}",

                styles["BodyText"]

            )

        )

        content.append(

            Paragraph(

                f"<b>Duration:</b> "
                f"{round(summary['duration_seconds'])} seconds",

                styles["BodyText"]

            )

        )

        content.append(

            Paragraph(

                f"<b>Negotiation Score:</b> "
                f"{summary['negotiation_score']}/100",

                styles["BodyText"]

            )

        )

        content.append(

            Paragraph(

                f"<b>Efficiency:</b> "
                f"{summary['efficiency']}",

                styles["BodyText"]

            )

        )

        content.append(

            Paragraph(

                f"<b>Quality:</b> "
                f"{summary['quality']}",

                styles["BodyText"]

            )

        )

        content.append(
            Spacer(1, 20)
        )

        # =====================================
        # AI Coach Analysis
        # =====================================

        content.append(

            Paragraph(

                "AI Coach Analysis",

                styles["Heading2"]

            )

        )

        content.append(
            Spacer(1, 10)
        )

        content.append(

            Paragraph(

                self.coach_feedback,

                styles["BodyText"]

            )

        )

        content.append(
            Spacer(1, 20)
        )

        # =====================================
        # Final Verdict
        # =====================================

        content.append(

            Paragraph(

                "Final Verdict",

                styles["Heading2"]

            )

        )

        content.append(
            Spacer(1, 10)
        )

        verdict = f"""
<b>Outcome:</b> {self.outcome}<br/>
<b>Efficiency:</b> {summary['efficiency']}<br/>
<b>Quality:</b> {summary['quality']}<br/>
<b>Overall Score:</b> {summary['negotiation_score']}/100
"""

        content.append(

            Paragraph(

                verdict,

                styles["BodyText"]

            )

        )

        content.append(
            Spacer(1, 20)
        )

        # =====================================
        # Transcript
        # =====================================

        content.append(

            Paragraph(

                "Conversation Transcript",

                styles["Heading2"]

            )

        )

        content.append(
            Spacer(1, 10)
        )

        transcript = (
            self.memory.get_transcript()
        )

        for msg in transcript:

            content.append(

                Paragraph(

                    f"<b>{msg['speaker']}:</b> "
                    f"{msg['message']}",

                    styles["BodyText"]

                )

            )

            content.append(
                Spacer(1, 5)
            )

        content.append(
            PageBreak()
        )

        doc.build(content)

        return filename