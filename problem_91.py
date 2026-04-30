#Price Calculator
import streamlit as st
price=st.number_input("Enter product price :")
level=st.slider("Enetr discount percentage :",0,50,5)
st.write(f"The amount of discount is :{level}")
if st.button("calculate"):
    st.write("Discounted price is :",price-((price*level)/100))
