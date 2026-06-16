
# =====================================
# metrics_panel.py
# =====================================

import streamlit as st


def metrics_panel():

    if "agent" not in st.session_state:

        return

    transcript = (
        st.session_state.agent.memory
        .get_transcript()
    )

    user_messages = len(

        [
            msg
            for msg in transcript
            if msg["speaker"] == "USER"
        ]

    )

    # =====================================
    # Deal Probability
    # =====================================

    probability = min(

        95,

        40 + (user_messages * 10)

    )

    # =====================================
    # History Tracking
    # =====================================

    if "probability_history" not in st.session_state:

        st.session_state.probability_history = []

    if (

        len(
            st.session_state.probability_history
        ) == 0

        or

        st.session_state.probability_history[-1]
        != probability

    ):

        st.session_state.probability_history.append(

            probability

        )

    st.markdown(
        "## 📊 Analytics Dashboard"
    )

    # =====================================
    # KPI Row
    # =====================================

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(

            "🎯 Deal Probability",

            f"{probability}%"

        )

    with col2:

        st.metric(

            "💬 Messages",

            len(transcript)

        )

    with col3:

        if len(transcript) >= 2:

            duration = (

                transcript[-1]["timestamp"]

                -

                transcript[0]["timestamp"]

            ).seconds

        else:

            duration = 0

        st.metric(

            "⏱ Duration",

            f"{duration}s"

        )

    st.progress(
        probability / 100
    )

    st.divider()

    # =====================================
    # Trend Chart
    # =====================================

    st.markdown(
        "### 📈 Deal Progress Trend"
    )

    chart_data = {

        "Probability":
        st.session_state.probability_history

    }

    st.line_chart(
        chart_data
    )

    st.divider()

    # =====================================
    # Negotiation Status
    # =====================================

    state = (

        st.session_state.agent
        .state_machine
        .get_state()

    )

    if state == "DEAL":

        st.success(
            "🏆 Agreement Reached"
        )

    elif state == "NO_DEAL":

        st.error(
            "❌ Negotiation Closed"
        )

    else:

        st.info(
            "🔄 Negotiation Active"
        )

