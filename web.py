import streamlit as st
import functions as func

todos = func.get_todos()
def add_todo():
    todo = st.session_state['new_todo']
    if todo != '':
        print(todo)
        todos.append(todo)
        func.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to improve your productivity")


for todo in todos:
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.remove(todo)
        func.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label=" ",placeholder="Add a new todo...",
              on_change=add_todo,key='new_todo')
