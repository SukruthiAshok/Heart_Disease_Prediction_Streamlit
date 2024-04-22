import streamlit as st

def logout():
    if 'session' in st.session_state:
        st.session_state.session = None
        st.success("You have been logged out successfully.")
    else:
        st.warning("You are already logged out.")
