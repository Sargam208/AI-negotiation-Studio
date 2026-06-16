# =====================================
# coach_panel.py
# =====================================

import streamlit as st
import sys
import os

project_root = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

sys.path.append(project_root)

from coach.llm_coach import (
    LLMCoach
)


# =====================================
# Coach Panel
# =====================================

def coach_panel():

    if "agent" not in st.session_state:

        return

    st.markdown(
        "## 🧠 AI Coach"
    )

    transcript = (
        st.session_state.agent.memory
        .get_transcript()
    )

    if len(transcript) < 2:

        st.info(
            "Start negotiating to receive coaching."
        )

        return

    coach = LLMCoach()

    try:

        feedback = coach.generate_feedback(

            transcript=transcript,

            scenario=st.session_state.get(
                "scenario",
                "Negotiation"
            )

        )

        st.success(
            feedback
        )

    except Exception as e:

        st.error(
            f"Coach unavailable: {e}"
        )