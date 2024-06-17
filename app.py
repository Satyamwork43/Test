import streamlit as st

x = st.slider('Select a value')
st.write(x, 'Length if x', len(x))
