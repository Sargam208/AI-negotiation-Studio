import streamlit as st

from theme import load_theme

from ui import (
    hero_section,
    persona_selector,
    scenario_selector
)
from chat_ui import negotiation_arena
from metrics_panel import metrics_panel
from coach_panel import coach_panel
from reporting.report_generator import ReportGenerator
from analytics.negotiation_analytics import (
    NegotiationAnalytics
)
st.set_page_config(

    page_title="AI Negotiation Studio",

    page_icon="🤝",

    layout="wide"

)

st.markdown(

    load_theme(),

    unsafe_allow_html=True

)

hero_section()

st.success(

    "🚀 UI Foundation Ready"

)

persona_selector()

scenario_selector()

if st.button(

    "🔄 Start New Negotiation",

    use_container_width=True

):

    if "agent" in st.session_state:

        del st.session_state.agent

    if "messages" in st.session_state:

        del st.session_state.messages

    if "celebrated" in st.session_state:
         del st.session_state.celebrated

    st.rerun()

st.divider()

# =====================================
# TABS
# =====================================

tab1, tab2, tab3, tab4 = st.tabs(

    [

        "💬 Negotiation",

        "📊 Analytics",

        "🧠 AI Coach",

        "📄 Reports"

    ]

)

# =====================================
# NEGOTIATION
# =====================================

with tab1:

    negotiation_arena()

# =====================================
# ANALYTICS
# =====================================

with tab2:

    metrics_panel()

# =====================================
# AI COACH
# =====================================

with tab3:

    coach_panel()

# =====================================
# REPORTS
# =====================================

# =====================================
# REPORTS TAB
# =====================================

# =====================================
# REPORTS TAB
# =====================================

with tab4:

    st.markdown(
        "## 📄 Negotiation Reports"
    )

    if "agent" not in st.session_state:

        st.info(
            "Start a negotiation first."
        )

    else:

        from coach.llm_coach import (
            LLMCoach
        )

        if st.button(

            "📄 Generate Report",

            use_container_width=True

        ):

            # -------------------------
            # Coach Feedback
            # -------------------------

            coach = LLMCoach()

            coach_feedback = (

                coach.generate_feedback(

                    transcript=
                    st.session_state.agent.memory
                    .get_transcript(),

                    scenario=
                    st.session_state.get(
                        "scenario",
                        "Unknown"
                    )

                )

            )

            # -------------------------
            # Analytics
            # -------------------------

            analytics = NegotiationAnalytics(

                st.session_state.agent.memory,

                st.session_state.agent.state_machine

            )

            # -------------------------
            # Report Generator
            # -------------------------

            generator = ReportGenerator(

                memory=
                st.session_state.agent.memory,

                scenario=
                st.session_state.get(
                    "scenario",
                    "Unknown"
                ),

                personality=
                st.session_state.get(
                    "personality",
                    "Unknown"
                ),

                outcome=
                st.session_state.agent
                .state_machine
                .get_state(),

                coach_feedback=
                coach_feedback,

                analytics=
                analytics

            )

            pdf_file = (
                generator.generate_pdf()
            )

            st.success(
                "Report generated successfully."
            )

            # -------------------------
            # Download Button
            # -------------------------

            with open(
                pdf_file,
                "rb"
            ) as f:

                st.download_button(

                    label=
                    "📥 Download Negotiation Report",

                    data=f,

                    file_name=
                    "Negotiation_Report.pdf",

                    mime=
                    "application/pdf",

                    use_container_width=True

                )

