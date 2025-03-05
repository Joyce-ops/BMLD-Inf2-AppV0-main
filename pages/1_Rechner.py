import streamlit as st

st.title("Rechner")

st.header("Berechnung von Stoffmengen")
st.number_input("Masse in g", 0.0)
st.number_input("Molare Masse in g/mol", 0.0)
st.write("Ergebnis: Stoffmenge in mol")

submitted = st.form_submit_button("Submit")
    
if submitted:
    
    result = calculate_stoffmenge(Masse / Molare Masse)
    
    st.write(f'Die Stoffmenge ist: {result["Stoffmenge"]} mol')
    st.write(f'Berechnet am: {result["timestamp"].strftime("%d.%m.%Y %H:%M:%S")}')

if st.button("Home"):
    st.switch_page("Start.py")
