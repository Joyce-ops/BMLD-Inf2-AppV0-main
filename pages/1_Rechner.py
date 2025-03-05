import streamlit as st

st.title("1_Rechner")

st.write("Berechnung von Stoffmengen")

if st.button("Home"):
    st.switch_page("Start.py")
if st.button("Rechner"):
    st.switch_page("pages/1_Rechner.py")