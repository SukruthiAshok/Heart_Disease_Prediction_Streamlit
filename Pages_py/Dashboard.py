import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import Predict as p
import login as log
import Home as h
import History as his

im = Image.open("favicon.ico")
st.set_page_config(page_title="HRUDAY",page_icon=im,layout="wide")
with st.sidebar:
    selected=option_menu(
        menu_title="Menu",
        options=["Account","Home","Predict","History","Logout"],
        icons=["box-arrow-in-right","house-fill","activity","clock-history","box-arrow-right"],
        default_index=0,
    )

if selected=="Account":
    log.login()
if selected=="Home":
    # st.title(f"{selected}")
    h.home()
if selected=="Predict":
    p.predict()
if selected=="History":
    his.history()
if selected=="Logout":
    st.write("Logged out Successfully!!!") 
