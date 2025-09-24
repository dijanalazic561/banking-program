
import functions
import time

FILE = "new_todo.txt"
now=time.strftime("%b,%d,%Y")
print("The time is below:")
print("It is", now)
while True:
    user_action = input("enter add/edit/delete/exit: ").strip().lower()
    try:
        match user_action:
            case "add":
                todo = input("Enter your todo: ").strip()
                try:
                    todos = functions.get_todos(FILE)
                except FileNotFoundError:
                    todos = []
                todos.append(todo + "\n")
                functions.write_todos(todos, FILE)
                print("added")

            case "show":
                try:
                    todos = functions.get_todos(FILE)
                    for index, item in enumerate(todos):
                        row = f"{index + 1}- {item.strip()}"
                        print(row)
                except FileNotFoundError:
                    print("Todos not found")

            case "edit":
                try:
                    todos = functions.get_todos(FILE)
                    nr = int(input("Enter a nr to edit: ")) - 1
                    if 0 <= nr < len(todos):
                        new_todo = input("Enter a new todo: ").strip()
                        todos[nr] = new_todo + "\n"
                        functions.write_todos(todos, FILE)
                        print("updated")
                    else:
                        print("Number out of range")
                except FileNotFoundError:
                    print("No todos found")
                except ValueError:
                    print("Enter a valid number")


            case "delete":
                try:
                    todos = functions.get_todos(FILE)
                    nr = int(input("Enter a number: ")) - 1  # convert to 0-based index
                    todos.pop(nr)
                    functions.write_todos(todos, FILE)
                    print("Deleted")
                except ValueError:
                    print("Please enter a valid number")
                except IndexError:
                    print("Number out of range")
                except FileNotFoundError:
                    print("No todos found")

            case "exit":
               print("Goodbye!")
               break
    except Exception as e:
        print("Error:",e)



