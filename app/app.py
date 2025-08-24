from helpers import run
import streamlit as st

st.header('Duplicate Question Pairs')
q1 = st.text_input('Enter Question 1')
q2 = st.text_input('Enter Question 2')

if st.button('Find'):
    print(q1, q2)
    response = run(q1, q2)
    print(response)
    if response:
        st.header("Duplicate")
    else:
        st.header("No Duplicate")
