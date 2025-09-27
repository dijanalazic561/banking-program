
FILE = "todos.txt"

def get_todos(filepath="todos.txt"):
    with open(filepath, "r", encoding="utf-8") as file:
        return[line.rstrip("\n") for line in file]


def write_todos(todos, filepath="todos.txt"):
    with open(filepath, "w",encoding="utf-8") as file:
        file.write("\n".join(todos) + ("\n" if todos else ""))

if __name__ == "__main__":
    print("Hello from functions")
    print(get_todos(FILE))