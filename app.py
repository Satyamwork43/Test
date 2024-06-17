import streamlit as st

x = st.text_input('Select a value')
st.write(x, 'Length if x', len(x))
