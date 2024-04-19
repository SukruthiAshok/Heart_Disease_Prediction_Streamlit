import streamlit as st
import pandas as pd
import Dashboard as d
from streamlit_option_menu import option_menu

#from st_pages import hide_pages
# st.set_page_config(page_title="HRUDAY",layout="wide")
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
                    st.success("You have successfully logged in")
                    # st.session_state["logged_in"] = True
                    # hide_pages([])
                    # st.success("Logged in!")
                    # st.switch_page("Pages_py/Dashboard.py")
		

def register_page():
    with st.form("register_form", clear_on_submit=True):
        st.subheader("Create New Account")
        new_user = st.text_input("Username")
        new_email = st.text_input("E-mail")
        new_password = st.text_input("Password", type='password')
        submitted = st.form_submit_button("Register")
        if submitted:
            if new_user == "" or new_email == "" or new_password == "":
                st.error("Fields cannot be empty!")
            else:
                # Register new user logic
                st.success("You have successfully created an Account")
 
def validate_login(username, password):
    # Add your login validation logic here
    # For simplicity, always return True in this example
    return True

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