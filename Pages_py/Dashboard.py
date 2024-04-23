import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import Predict as p
import login as log
import Home as h
<<<<<<< HEAD
from session_state import SessionState
=======
import History as his
>>>>>>> 6a732878397b904784763a345620d46108e8f217

im = Image.open("favicon.ico")
st.set_page_config(page_title="HRUDAY",page_icon=im,layout="wide")
user_id = None
with st.sidebar:
    selected=option_menu(
        menu_title="Menu",
        options=["Account","Home","Predict","History","Logout"],
        icons=["box-arrow-in-right","house-fill","activity","clock-history","box-arrow-right"],
        default_index=0,
    )
def process_data(user_id):
    global user_id
    user_id = userid

if selected=="Account":
    log.login()
if selected=="Home":
    # st.title(f"{selected}")
    h.home()
if selected=="Predict":
    p.predict()
if selected=="History":
<<<<<<< HEAD
    st.title(f"{selected}")
if selected=="Logout":
    user_id = None
=======
    his.history()
if selected=="Logout":
    st.write("Logged out Successfully!!!") 
>>>>>>> 6a732878397b904784763a345620d46108e8f217
