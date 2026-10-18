import streamlit as st

st.title("Login Page")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username == "admin " and password == "12345":
        st.success("Login Successful")
    else:
        st.error("Invalid Credentials")