import streamlit as st

st.title("Stoffmengenrechner")

st.header("Berechnung von Stoffmengen")


def calculate_Stoffmenge(Masse, Molaremasse):
    Stoffmenge = Masse / Molaremasse

    return Stoffmenge
    

with st.form("Stoffmenge berechner"):
    Masse = st.number_input('Geben Sie die Masse ein (in Gramm)', min_value=0.0001, max_value=10000.0, value=10.0, step=0.0001)
    Molaremasse = st.number_input('Geben Sie die Molaremasse ein (in g/mol)', min_value=1.0, max_value=500.0, value=1.008, step=0.0001)

    submitted = st.form_submit_button("Submit")
    
if submitted:
    
    result = calculate_Stoffmenge(Masse, Molaremasse)
    
    st.write(f'Die Stoffmenge ist: {result}')

if st.button("Home"):
    st.switch_page("Start.py")