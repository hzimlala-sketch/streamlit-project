import streamlit as st

st.title("button Example")

st.write("Welcome to Streamlit!")

matricNum = st.text_input("your matric number", "Type Here ...")

if st.button("Submit"):
    st.success(f"your matric number is {matricNum}!")