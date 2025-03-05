import streamlit as st

st.title("Unterseite B")

st.write("Diese Seite ist eine Unterseite der Startseite.")

if st.button("Home"):
    st.switch_page("Start.py")

def calculate_Stoffmenge(Masse, Molaremasse):
    Stoffmenge = Masse / Molaremasse

with st.form("Stoffmenge berechner"):
    Masse = st.number_input('Geben Sie die Masse ein (in Gramm)', min_value=0.001, max_value=10000.0, value=1.7, step=0.01)
    Molaremasse = st.number_input('Geben Sie die Molaremasse ein (in g/mol)', min_value=1.0, max_value=500.0, value=70.0, step=0.1)

    submitted = st.form_submit_button("Submit")
    
if submitted:
    
    result = calculate_Stoffmenge(Masse, Molaremasse)
    
    st.write(f'Die Stoffmenge ist: {result["Stoffmenge"]}')
    st.write(f'Berechnet am: {result["timestamp"].strftime("%d.%m.%Y %H:%M:%S")}')