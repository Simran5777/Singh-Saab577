def write_notes():
    with open("notes.txt", "w") as file:
        note = input("Enter a note: ")
        file.write(note + "\n")

def read_notes():
    try:
        with open("notes.txt", "r") as file:
            print("Notes:")
            print(file.read())
    except FileNotFoundError:
        print("No notes found.")

def append_notes():
    with open("notes.txt", "a") as file:
        note = input("Enter a note to append: ")
        file.write(note + "\n")

write_notes()
read_notes()
append_notes()
read_notes()
