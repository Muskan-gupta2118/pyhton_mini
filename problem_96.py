#Temperature converter
import streamlit as st

st.title("Temperature Converter")

temp = st.number_input("Enter Temperature")

option = st.selectbox("Convert to", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])

if option == "Celsius to Fahrenheit":
    result = (temp * 9/5) + 32
else:
    result = (temp - 32) * 5/9

st.write("Converted Temperature:", result)