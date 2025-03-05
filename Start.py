import streamlit as st
import pandas as pd

st.title("Meine erste Streamlit App")

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
if st.button("Rechner"):
    st.switch_page("pages/1_Rechner.py")