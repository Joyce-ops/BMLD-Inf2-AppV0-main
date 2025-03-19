from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')  

import streamlit as st

st.title("Rechner")

st.header("Berechnung von Stoffmengen")


def calculate_Stoffmenge(Masse, Molaremasse):
    Stoffmenge = Masse / Molaremasse

    return Stoffmenge
    

with st.form("Stoffmenge berechner"):
    Masse = st.number_input('Geben Sie die Masse ein (in Gramm)', min_value=0.001, max_value=1000.0, value=10.000, step=0.001)
    Molaremasse = st.number_input('Geben Sie die Molaremasse ein (in g/mol)', min_value=1.0, max_value=500.0, value=1.008, step=0.001)

    submitted = st.form_submit_button("Submit")
    
if submitted:
    
    result = calculate_Stoffmenge(Masse, Molaremasse)
    
    st.write(f'Die Stoffmenge ist: {result} mol')

if st.button("Home"):
    st.switch_page("Start.py")


import streamlit as st

st.markdown(
    """
    <style>
    .stForm {
        background-color: #7CA9BD;
        padding: 20px;
        border-radius: 10px;
    }
    .stForm div {
        color: white;  /* Optional: Textfarbe ändern, damit sie besser lesbar ist */
    }
    </style>
    """,
    unsafe_allow_html=True
)

 # Save data
from utils.data_manager import DataManager
DataManager().append_record(session_state_key='data_df', record_dict={'Masse': Masse, 'Molaremasse': Molaremasse, 'Stoffmenge': result})  # update data in session state and storage

