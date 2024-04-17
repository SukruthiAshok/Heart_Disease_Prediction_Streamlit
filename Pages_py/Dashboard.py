import streamlit as st
from streamlit_option_menu import option_menu
import Predict as p
import login as log
st.set_page_config(page_title="HRUDAY",layout="wide")

with st.sidebar:
    selected=option_menu(
        menu_title="Menu",
        options=["Account","Home","Predict","History","Logout"],
        icons=["box-arrow-in-right","house-fill","activity","clock-history","box-arrow-right"],
        default_index=0,
    )

if selected=="Account":
    log.main()
if selected=="Home":
    st.title(f"{selected}")
if selected=="Predict":
    p.main()
if selected=="History":
    st.title(f"{selected}")        