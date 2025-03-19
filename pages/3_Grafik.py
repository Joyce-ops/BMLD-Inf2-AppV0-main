# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')  
# ====== End Login Block ======

# ------------------------------------------------------------
# === BMI Grafik ===
import streamlit as st

st.title('Stoffmengen Werte')

data_df = st.session_state['data_df']
if data_df.empty:
    st.info('Keine Daten vorhanden. Berechnen Sie Ihre SToffmenge auf der Startseite.')
    st.stop()

# Masse
st.line_chart(data=data_df.set_index['masse'], 
                use_container_width=True)
st.caption('Masse (g)')

# Molare Masse
st.line_chart(data=data_df.set_index['Molaremasse'],
                use_container_width=True)
st.caption('Molaremasse (g/mol)')

# Stoffmengen
st.line_chart(data=data_df.set_index['Stoffmengen'],
                use_container_width=True)
st.caption('Stoffmenge über Zeit')