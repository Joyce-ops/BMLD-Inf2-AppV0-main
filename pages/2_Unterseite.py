import streamlit as st

st.title("Unterseite B")

st.write("Diese Seite ist eine Unterseite der Startseite.")

if st.button("Home"):
    st.switch_page("Start.py")

