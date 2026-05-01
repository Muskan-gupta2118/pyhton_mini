#Simple to do list
import streamlit as st

st.title("To-Do List")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

task = st.text_input("Enter a task")

if st.button("Add Task"):
    st.session_state.tasks.append(task)

st.write("Your Tasks:")
for t in st.session_state.tasks:
    st.write("- ", t)