import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from table_model import cursor, connection
import bcrypt
from session_state import SessionState
import Predict

##from st_pages import hide_pages
# st.set_page_config(page_title="HRUDAY",layout="wide")
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
                        d.process_data(user_id)
                        st.success("You have successfully logged in")
                    else:
                        st.error("Invalid username or password!")


def register_page():
    with st.form("register_form", clear_on_submit=True):
        st.subheader("Create New Account")
        new_user = st.text_input("Username")
        new_email = st.text_input("E-mail")
        new_password = st.text_input("Password", type='password')
        hashPass = hash_password(new_password)
        submitted = st.form_submit_button("Register")
        if submitted:
            if new_user == "" or new_email == "" or new_password == "":
                st.error("Fields cannot be empty!")
            else:
                # Register new user logic
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


# if __name__ == '__main__':
#     main()























# Security
#passlib,hashlib,bcrypt,scrypt
# import hashlib
# def make_hashes(password):
# 	return hashlib.sha256(str.encode(password)).hexdigest()

# def check_hashes(password,hashed_text):
# 	if make_hashes(password) == hashed_text:
# 		return hashed_text
# 	return False
# # DB Management
# import sqlite3 
# conn = sqlite3.connect('heartdp.db')
# c = conn.cursor()
# # DB  Functions
# def create_usertable():
# 	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


# def add_userdata(username,password):
# 	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
# 	conn.commit()

# def login_user(username,password):
# 	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
# 	data = c.fetchall()
# 	return data


# def view_all_users():
# 	c.execute('SELECT * FROM userstable')
# 	data = c.fetchall()
# 	return data

# menu = ["Home","Login","SignUp"]
# choice = st.sidebar.selectbox("Menu",menu)

# if choice == "Home":
# 	st.subheader("Home")

# elif choice == "Login":
	
# 	st.sidebar.subheader("Login Section")
# 	username = st.sidebar.text_input("User Name")
# 	password = st.sidebar.text_input("Password",type='password')
# 	if st.sidebar.checkbox(label="Login"):
# 		# if password == '12345':
# 		create_usertable()
# 		hashed_pswd = make_hashes(password)

# 		result = login_user(username,check_hashes(password,hashed_pswd))
# 		if result:
# 			st.sidebar.success("Logged In as {}".format(username))
# 			if result:
# 				d.dashboard()

# 		else:
# 			st.warning("Incorrect Username/Password")

# elif choice == "SignUp":
# 	st.subheader("Create New Account")
# 	new_user = st.text_input("Username")
# 	new_password = st.text_input("Password",type='password')

# 	if st.button("Signup"):
# 		create_usertable()
# 		add_userdata(new_user,make_hashes(new_password))
# 		st.success("You have successfully created a valid Account")
# 		st.info("Go to Login Menu to login")