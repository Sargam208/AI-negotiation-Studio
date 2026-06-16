# =====================================
# ui.py
# =====================================
import sys
import os

project_root = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

sys.path.append(project_root)
import streamlit as st
from scenarios.scenario_manager import ScenarioManager
from session_manager import reset_negotiation


def hero_section():

    st.markdown(

        """
        <div class='hero'>

        <h1>
        🤝 AI Negotiation Studio
        </h1>

        <h4>
        Smart Negotiations.
        Human-Like Strategy.
        AI-Powered Decisions.
        </h4>

        </div>
        """,

        unsafe_allow_html=True

    )




def persona_selector():

    st.markdown("## 🎭 Choose Your Negotiator")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button(
            "🤝\n\nDIPLOMAT",
            use_container_width=True
        ):
            reset_negotiation()
            st.session_state.personality = "DIPLOMAT"

    with col2:
        if st.button(
            "⚖️\n\nSTRATEGIST",
            use_container_width=True
        ):
            reset_negotiation()
            st.session_state.personality = "STRATEGIST"

    with col3:
        if st.button(
            "🛡️\n\nGUARDIAN",
            use_container_width=True
        ):
            reset_negotiation()
            st.session_state.personality = "GUARDIAN"

    with col4:
        if st.button(
            "♟️\n\nTITAN",
            use_container_width=True
        ):
            reset_negotiation()
            st.session_state.personality = "TITAN"

    if "personality" not in st.session_state:
        st.session_state.personality = "STRATEGIST"

    st.success(
        f"Selected: {st.session_state.personality}"
    )



def scenario_selector():

    manager = ScenarioManager()

    st.markdown("## 🎯 Choose Scenario")

    col1, col2, col3, col4, col5 = st.columns(5)

    scenarios = {

        "SALARY": "💼 Salary",

        "FREELANCE": "💻 Freelance",

        "CAR": "🚗 Car",

        "RENT": "🏠 Rent",

        "PRODUCT": "📦 Product"

    }

    columns = [col1, col2, col3, col4, col5]

    for idx, (key, label) in enumerate(scenarios.items()):

        with columns[idx]:

            if st.button(
                label,
                use_container_width=True
            ):
                reset_negotiation()

                st.session_state.scenario = key

    if "scenario" not in st.session_state:

        st.session_state.scenario = "SALARY"

    scenario = manager.get_scenario(

        st.session_state.scenario

    )

    st.info(
f"""
Role: {scenario['role']}

Goal: {scenario['goal']}
"""
)