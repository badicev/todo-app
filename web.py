import streamlit as st
import functions as f

todo_list = f.get_todos()

def clear_text():
    st.session_state["new_todo"] = ""

def add_todo():
    todo = st.session_state["new_todo"] + "\n" #session_state is a type of streamlit that is similar to dictionary
    print(todo)
    todo_list.append(todo)
    f.write_todos(todo_list)


st.title("To-do App")
st.subheader("")
st.write("Increase your productivity.")

for index, todo in enumerate(todo_list):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todo_list.pop(index)
        f.write_todos(todo_list)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Add a new to-do: ", placeholder="Type something...",
              on_change=add_todo, key='new_todo')
st.button("Clear", on_click=clear_text)

