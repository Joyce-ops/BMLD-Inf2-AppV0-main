import streamlit as st

st.title("Rechner")

st.header("Berechnung von Stoffmengen")
st.number_input("Masse in g", 0.0)
st.number_input("Molare Masse in g/mol", 0.000)
st.write("Ergebnis: Stoffmenge in mol")

submitted = st.form_submit_button("Submit")


if st.button("Home"):
    st.switch_page("Start.py")
