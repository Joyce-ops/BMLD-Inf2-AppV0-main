import streamlit as st

st.title("Unterseite B")

st.write("Diese Seite ist eine Unterseite der Startseite.")

if st.button("Home"):
    st.switch_page("Start.py")
if st.button("Rechner Stoffmenge"):
    st.switch_page("pages/1_Rechner.py")