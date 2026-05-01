#student marks dashboard
import streamlit as st

st.title("Student Marks Dashboard")

students = ["Aman", "Riya", "John"]

marks = {
    "Aman": 85,
    "Riya": 92,
    "John": 78
}

selected_student = st.selectbox("Select Student", students)

st.metric("Marks", marks[selected_student])

st.bar_chart(list(marks.values()))