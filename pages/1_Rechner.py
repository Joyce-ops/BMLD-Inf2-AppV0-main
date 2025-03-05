import streamlit as st

st.title("1_Rechner")

st.write("Berechnung von Stoffmengen")
st.number_input("Masse in g", 0.0)
st.number_input("Molare Masse in g/mol", 0.0)
if molare_masse != 0:
    stoffmenge = masse / molare_masse
    st.write(f"Stoffmenge: {stoffmenge} mol")
else:
    st.write("Bitte gib eine gültige molare Masse ein.")


if st.button("Home"):
    st.switch_page("Start.py")
if st.button("Rechner"):
    st.switch_page("pages/1_Rechner.py")