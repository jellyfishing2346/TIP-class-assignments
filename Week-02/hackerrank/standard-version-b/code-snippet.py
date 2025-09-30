students = ["Samarth", "Nicolas", "Lexie", "Theresa"]
next_id = 12348
directory = {12345: "Samarth", 12346: "Nicolas", 12347: "Lexie"}
for student in students:
    if student in directory.values():
        directory[next_id] = student
        next_id += 1
print(directory[12348])
