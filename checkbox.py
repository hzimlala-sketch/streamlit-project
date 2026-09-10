import streamlit as st

st.title("checkbox Example")



agree = st.checkbox("i agree")
disagree = st.checkbox("i disagree")

if agree:
    st.write("You agreed!")
elif disagree:
    st.write("You disagreed!")

