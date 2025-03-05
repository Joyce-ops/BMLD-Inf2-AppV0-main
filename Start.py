import streamlit as st
import pandas as pd

st.title("Stoffmengenrechner")
st.write("Hier kannst du per Eingabe von Masse und Molare Masse die Stoffmenge berechnen.")
if st.button("Rechner Stoffmenge"):
    st.switch_page("pages/1_Rechner.py")
# !! WICHTIG: Eure Emails müssen in der App erscheinen!!

# Streamlit über den Text unten direkt in die App - cool!
"""
Diese App wurde von folgenden Personen entwickelt:
- Joyce Baumann (Baumajoy@students.zhaw.ch)
- Mcqulat Miller (millemcq@students.zhaw.ch)

"""

