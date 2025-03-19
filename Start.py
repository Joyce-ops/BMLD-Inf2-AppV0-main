import streamlit as st
import pandas as pd
from utils.data_manager import DataManager
from utils.login_manager import LoginManager

# initialize the data manager
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="BMLD_App_DB")  # switch drive 

login_manager = LoginManager(data_manager)
login_manager.login_register()  # open login/register page

# load the data from the persistent storage into the session state
data_manager.load_user_data(
    session_state_key='data_df', 
    file_name='data.csv', 
    initial_value = pd.DataFrame(), 
    )

# === Initialize the login manager ===
from utils.login_manager import LoginManager

login_manager = LoginManager(data_manager) # initialize login manager
login_manager.login_register()  # opens login page


# === Main page ===
import streamlit as st

st.title("Stoffmengenrechner")
st.subheader("Willkommen beim Stoffmengen-Rechner!")
st.info("Berechnen Sie schnell und einfach die benötigten Mengen für Ihre Materialien. Ob für Projekte, Produktionen oder den täglichen Bedarf unser Tool hilft Ihnen, präzise und effizient zu planen.")

st.write("Legen Sie direkt los und optimieren Sie Ihre Berechnungen!")
if st.button("Hier gehts zum Rechner"):
    st.switch_page("pages/1_Rechner.py")

"""
Diese App wurde von folgenden Personen entwickelt:
- Joyce Baumann (Baumajoy@students.zhaw.ch)
- Mcqulat Miller (millemcq@students.zhaw.ch)

"""
image_url = "https://cdn.pixabay.com/photo/2016/08/28/16/26/periodic-table-1626299_1280.png"
st.image(image_url, caption="Periodensystem", use_container_width=True)

# !! WICHTIG: Eure Emails müssen in der App erscheinen!!

# Streamlit über den Text unten direkt in die App - cool!
