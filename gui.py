import functions
import FreeSimpleGUI as sg
label=sg.Text("Type in a todo")
input_box=sg.InputText(tooltip="Enter a todo", key="todo")
add_button=sg.Button("Add")
list_box=sg.Listbox(values=functions.get_todos("todos.txt"), key="todos",
                    enable_events=True, size=(45,10))
edit_button=sg.Button("Edit")
window=sg.Window("My todo app",
                 layout=[[label], [input_box, add_button],[list_box, edit_button]],
                 font=("Helvetica",20))
while True:
    event, values = window.read()
    if event in(sg.WIN_CLOSED,None):
        break
    if not isinstance(values,dict):
        continue
    event,values=window.read()
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
        case "Edit":
            todo_to_edit=values["todos"][0]
            new_todo=values["todo"].strip()
            todos=functions.get_todos("todos.txt")
            index = todos.index(todo_to_edit)
            todos[index]=new_todo
            functions.write_todos(todos,filepath="todos.txt")
            window["todos"].update(values=todos)
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case sg.WIN_CLOSED:
            break
window.close()



