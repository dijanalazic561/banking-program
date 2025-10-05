import time
import functions
import FreeSimpleGUI as sg
sg.theme("LightBrown5")

now=time.strftime("%b %d, %Y in %H:%M:%S")
clock=sg.Text("", key="clock")
label=sg.Text("Type in a todo")
input_box=sg.InputText(tooltip="Enter a todo", key="todo")
add_button=sg.Button("Add")
list_box=sg.Listbox(values=functions.get_todos("todos.txt"), key="todos",
                    enable_events=True, size=(45,10))
edit_button=sg.Button("Edit")
delete_button=sg.Button("Delete")
exit_button=sg.Button("Exit")
window=sg.Window("My todo app",
                 layout=[[clock],
                         [label],
                         [input_box, add_button],
                         [list_box, edit_button, delete_button],
                         [exit_button]],
                 font=('Helvetica', 20))
while True:
    event, values = window.read(timeout=100)
    window["clock"].update(value=time.strftime("%b %d, %Y in %H:%M:%S"))
    if event in(sg.WIN_CLOSED,None):
        break

    print(1,event)
    print(2,values)
    print(3,values["todos"])

    match event:
        case "Add":
            todos=functions.get_todos("todos.txt")
            new_todo = values['todo'].strip()
            if new_todo:
                todos.append(new_todo)
                functions.write_todos(todos,"todos.txt")
                window["todos"].update(values=todos)
                window["todo"].update(value='')
        case "Edit":
            try:
                todo_to_edit=values["todos"][0]
                new_todo=values["todo"].strip()
                todos=functions.get_todos("todos.txt")
                index = todos.index(todo_to_edit)
                todos[index]=new_todo
                functions.write_todos(todos,filepath="todos.txt")
                window["todos"].update(values=todos)
                window["todo"].update(value='')
            except IndexError:
                sg.popup("Select the item first", font=("Helvetica", 20))
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case "Delete":
            try:
                todo_to_delete=values["todos"][0]
                todos=functions.get_todos("todos.txt")
                todos.remove(todo_to_delete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value='')
            except IndexError:
                sg.popup("Missing item to delete", font=("Helvetica", 20))
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
window.close()



