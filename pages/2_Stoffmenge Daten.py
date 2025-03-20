# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')  
# ====== End Login Block ======

# ------------------------------------------------------------
# Here starts the actual app, which was developed previously
import streamlit as st

st.title('Stoffmengen Werte')

data_df = st.session_state['data_df']
if data_df.empty:
    st.info('Keine Daten vorhanden. Berechnen Sie Ihre Stoffmenge auf der Startseite.')
    st.stop()


# Display table
st.dataframe(data_df)

if st.button("Home"):
    st.switch_page("Start.py")