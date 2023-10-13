def creating_to_do_list():
    notes_list = [""] * 10  # the tasks will always be maximum 10
    while True:
        command = input()
        if command == "End":
            return notes_list
        note = command.split("-")
        notes_list[int(note[0]) - 1] = note[1]


to_do_list = [x for x in creating_to_do_list() if x != ""]
print(to_do_list)
