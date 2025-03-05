import streamlit as st

st.title("Rechner")

st.header("Berechnung von Stoffmengen")
st.number_input("Masse in g", 0.0)
st.number_input("Molare Masse in g/mol", 0.0)
st.write("Ergebnis: Stoffmenge in mol")
if molare_masse != 0:
    stoffmenge = masse / molare_masse
else:
    stoffmenge = 0

# Ergebnis anzeigen
st.write(f"Ergebnis: Stoffmenge in mol = {stoffmenge}")

if st.button("Home"):
    st.switch_page("Start.py")
if st.button("Rechner 2"):
    st.switch_page("pages/2_Rechner.py")

if st.button("Home"):
    st.switch_page("Start.py")
if st.button("Rechner 2"):
    st.switch_page("pages/2_Rechner.py")