import streamlit as st
import pandas as pd
import re
from streamlit_option_menu import option_menu
from table_model import cursor, connection
import bcrypt
from session_state import SessionState
import Predict
import History


def hash_password(password):
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def verify_password(plain_password, hashed_password):
    # Check if the plain password matches the hashed password
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))


def login():
    # st.title("Hruday")
    
    selected = option_menu(
        menu_title=None,
        options=["LOGIN", "REGISTER"],
        orientation="horizontal"
    )

    if selected == "LOGIN":
        login_page()
    elif selected == "REGISTER":
        register_page()

def login_page():
    with st.form("login_form", clear_on_submit=True):
        st.subheader("LOGIN")
        user_name = st.text_input("Username ")
        pwd = st.text_input("Password ", type='password')
        log = st.form_submit_button("Login")
        if log:
            if user_name == "" or pwd == "":
                st.error("Username and password cannot be empty!")
            else:
                    if validate_login(user_name, pwd):
                        # Create or retrieve session state
                        sessionState = SessionState(username=user_name,password=pwd)
                        user_id = sessionState.return_userid()
                        Predict.process_data(user_id)
                        History.process_data(user_id)
                        st.success("You have successfully logged in")
                    else:
                        st.error("Invalid username or password!")

def is_valid_email(email):
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(regex, email)

def is_valid_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter"
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter"
    if not re.search(r'[0-9]', password):
        return False, "Password must contain at least one digit"
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Password must contain at least one special character"
    return True, ""

def register_page():
    with st.form("register_form", clear_on_submit=True):
        st.subheader("Create New Account")
        new_user = st.text_input("Username")
        new_email = st.text_input("E-mail")
        new_password = st.text_input("Password", type='password')
        hashPass = hash_password(new_password)
        submitted = st.form_submit_button("Register")
        if submitted:
            if not new_user or not new_email or not new_password:
                st.error("Please fill out all fields")
            elif not is_valid_email(new_email):
                st.error("Please enter a valid email address")
            else:
                is_valid, message = is_valid_password(new_password)
                if not is_valid:
                    st.error(message)
                else:
                    st.success("You have successfully created an Account")
                    data = (new_user, new_email, hashPass)
                    sql = "INSERT INTO user (username, email, password) VALUES (%s,%s,%s)"
                    cursor.execute(sql,data)
                    connection.commit()
        
 
def validate_login(username, password):
    # Query the database to retrieve the hashed password for the provided username
    sql = "SELECT password FROM user WHERE username = %s"
    cursor.execute(sql, (username,))
    result = cursor.fetchone()

    if result:
        hashed_password = result[0]  # Extract the hashed password from the result
        # Verify the provided password against the hashed password using your existing function
        if verify_password(password, hashed_password):
            return True  # Return True if the passwords match
    return False  # Return False if no matching user or password mismatch
