def naughty_or_nice_list(names, *args, **kwargs):
    kids = {
        "Nice": [],
        "Naughty": [],
        "Not found": []
    }

    for command in args:
        command = command.split("-")
        number = int(command[0])
        behaviour = command[1]

        current_names = []
        kid_number = 0

        for kid in names:
            if number == kid[0]:
                kid_number = number
                current_names.append(kid[1])

        if len(current_names) == 1:
            names.remove((kid_number, current_names[0]))
            kids[behaviour].append(current_names[0])

    for (name, behaviour) in kwargs.items():
        current_names = []
        kid_number = 0
        for kid in names:
            if name == kid[1]:
                kid_number = kid[0]
                current_names.append(kid[1])

        if len(current_names) == 1:
            names.remove((kid_number, current_names[0]))
            kids[behaviour].append(current_names[0])

    for kid in names:
        kids["Not found"].append(kid[1])

    string_to_print = ""
    for (behaviour, kids_list) in kids.items():
        if kids_list:
            string_to_print += f"{behaviour}: {', '.join(kids_list)}\n"

    return string_to_print


print(naughty_or_nice_list([(3, "Amy"), (1, "Tom"), (7, "George"), (3, "Katy"), ],
                           "3-Nice", "1-Naughty",
                           Amy="Nice", Katy="Naughty", ))

print(naughty_or_nice_list([(7, "Peter"), (1, "Lilly"), (2, "Peter"), (12, "Peter"), (3, "Simon"), ],
                           "3-Nice", "5-Naughty", "2-Nice", "1-Nice", ))

print(naughty_or_nice_list([(6, "John"), (4, "Karen"), (2, "Tim"), (1, "Merry"), (6, "Frank"), ],
                           "6-Nice", "5-Naughty", "4-Nice", "3-Naughty", "2-Nice", "1-Naughty",
                           Frank="Nice", Merry="Nice", John="Naughty", ))
