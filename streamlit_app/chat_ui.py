# =====================================
# chat_ui.py
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

from agent.negotiation_agent import NegotiationAgent
from scenarios.scenario_manager import ScenarioManager


# =====================================
# Initialize Agent
# =====================================

def initialize_agent():

    manager = ScenarioManager()

    scenario = manager.get_scenario(
        st.session_state.scenario
    )

    if "agent" not in st.session_state:

        st.session_state.agent = NegotiationAgent(

            personality=
            st.session_state.personality,

            scenario=
            scenario["title"]

        )

    if "messages" not in st.session_state:

        st.session_state.messages = []

    if "celebrated" not in st.session_state:

        st.session_state.celebrated = False


# =====================================
# Negotiation Arena
# =====================================

def negotiation_arena():

    initialize_agent()

    st.markdown(
        "## 💬 Negotiation Arena"
    )

    # =====================================
    # Current State Banner
    # =====================================

    current_state = (

        st.session_state.agent
        .state_machine
        .get_state()

    )

    if current_state == "DEAL":

        st.success(

            """
🏆 Negotiation Completed Successfully

🤝 Agreement Reached Between Both Parties
            """

        )

    elif current_state == "NO_DEAL":

        st.warning(

            """
Negotiation Closed

No agreement was reached.
            """

        )

    # =====================================
    # Chat History
    # =====================================

    for msg in st.session_state.messages:

        with st.chat_message(
            msg["role"]
        ):

            st.write(
                msg["content"]
            )

    # =====================================
    # Disable Input After Completion
    # =====================================

    if current_state in [

        "DEAL",

        "NO_DEAL"

    ]:

        st.info(
            "Negotiation has ended. Start a new negotiation to continue."
        )

        return

    # =====================================
    # User Input
    # =====================================

    user_input = st.chat_input(
        "Make an offer..."
    )

    if user_input:

        # -----------------------------
        # User Message
        # -----------------------------

        st.session_state.messages.append(

            {

                "role": "user",

                "content": user_input

            }

        )

        with st.chat_message(
            "user"
        ):

            st.write(
                user_input
            )

        # -----------------------------
        # Agent Response
        # -----------------------------

        result = (

            st.session_state.agent.respond(
                user_input
            )

        )

        state = result["state"]

        response = result["response"]

        st.session_state.messages.append(

            {

                "role": "assistant",

                "content": response

            }

        )

        with st.chat_message(
            "assistant"
        ):

            st.write(
                response
            )

        # =====================================
        # Celebration
        # =====================================

        if (

            state == "DEAL"

            and

            not st.session_state.celebrated

        ):

            

            st.toast(

                "🏆 Agreement successfully finalized."

            )

            st.session_state.celebrated = True

        elif (

            state == "NO_DEAL"

            and

            not st.session_state.celebrated

        ):

            st.toast(

                "Negotiation closed."

            )

            st.session_state.celebrated = True

        st.rerun()

