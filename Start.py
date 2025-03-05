import streamlit as st
import pandas as pd

st.title("Stoffmengenrechner")
st.write("Hier kannst du per Eingabe von Masse und Molare Masse die Stoffmenge berechnen.")
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
