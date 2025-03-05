import streamlit as st
import pandas as pd

st.title("App von Joyce und Mcqulat")
st.write("Willkommen zur App von Joyce und Mcqulat. Hier kannst du einen Rechner finden, die dir im Chemie-Alltag helfen können.")

if st.button("Rechner Stoffmenge"):
    st.switch_page("pages/1_Rechner.py")
# !! WICHTIG: Eure Emails müssen in der App erscheinen!!

# Streamlit über den Text unten direkt in die App - cool!
"""
Diese App wurde von folgenden Personen entwickelt:
- Joyce Baumann (Baumajoy@students.zhaw.ch)
- Mcqulat Miller (millemcq@students.zhaw.ch)

Autoren: 
- Joyce Baumann (Baumajoy@students.zhaw.ch)
- Mcqulat Miller (millemcq@students.zhaw.ch)
"""

