import streamlit as st

def home():
    st.title("Welcome to HRUDAY - Heart Disease Prediction App")
    st.write("""
    This app predicts the likelihood of heart disease based on various input features.
    You can use the navigation menu on the left to explore different sections of the app.
    """)
    st.image("logo.jpg", caption="Heart Disease Prediction", use_column_width=True)

if __name__ == "__main__":
    home()
