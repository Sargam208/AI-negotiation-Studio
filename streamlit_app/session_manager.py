import streamlit as st


def reset_negotiation():

    keys_to_remove = [

        "agent",

        "messages",

        "analytics",

        "report",

        "achievements"

    ]

    for key in keys_to_remove:

        if key in st.session_state:

            del st.session_state[key]