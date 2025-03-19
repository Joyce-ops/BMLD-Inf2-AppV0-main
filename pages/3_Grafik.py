# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')  
# ====== End Login Block ======

# ------------------------------------------------------------
import streamlit as st

# Titel der Seite
st.title('Stoffmengen Werte')

# Laden des DataFrames aus st.session_state
data_df = st.session_state.get('data_df', None)

# Überprüfen, ob der DataFrame vorhanden ist und Daten enthält
if data_df is None or data_df.empty:
    st.info('Keine Daten vorhanden. Berechnen Sie Ihre Stoffmenge auf der Startseite.')
    st.stop()

# Debug: Spaltennamen des DataFrames ausgeben
st.write("Verfügbare Spalten:", data_df.columns)

# Masse
if 'masse' in data_df.columns:
    st.line_chart(data=data_df.set_index('masse'), use_container_width=True)
    st.caption('Masse (g)')
else:
    st.warning("Spalte 'masse' nicht gefunden.")

# Molare Masse
if 'Molaremasse' in data_df.columns:
    st.line_chart(data=data_df.set_index('Molaremasse'), use_container_width=True)
    st.caption('Molaremasse (g/mol)')
else:
    st.warning("Spalte 'Molaremasse' nicht gefunden.")

# Stoffmengen
if 'Stoffmengen' in data_df.columns:
    st.line_chart(data=data_df.set_index('Stoffmengen'), use_container_width=True)
    st.caption('Stoffmenge über Zeit')
else:
    st.warning("Spalte 'Stoffmengen' nicht gefunden.")