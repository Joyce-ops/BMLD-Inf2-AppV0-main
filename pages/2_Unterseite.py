import streamlit as st

st.title("Unterseite B")

st.write("Diese Seite ist eine Unterseite der Startseite.")

if st.button("Home"):
    st.switch_page("Start.py")

with st.form("BMI Eingabeformular"):
    # Get user input for height and weight
    height = st.number_input('Geben Sie Ihre Größe ein (in Meter)', min_value=0.1, max_value=3.0, value=1.7, step=0.01)
    weight = st.number_input('Geben Sie Ihr Gewicht ein (in kg)', min_value=1.0, max_value=500.0, value=70.0, step=0.1)

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    
if submitted:
    
    result = calculate_bmi(height, weight)
    
    st.write(f'Ihr BMI ist: {result["bmi"]}')
    st.write(f'Berechnet am: {result["timestamp"].strftime("%d.%m.%Y %H:%M:%S")}')
    st.write(f'Kategorie: {result["category"]}')