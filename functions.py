
FILE = "new_todo.txt"

def get_todos(filepath):
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos

def write_todos(todos_arg, filepath):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello from functions")
    print(get_todos(FILE))