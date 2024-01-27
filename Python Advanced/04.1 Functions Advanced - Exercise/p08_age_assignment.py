def age_assignment(*args, **kwargs):
    names_with_ages = {}
    for name in args:
        names_with_ages[name] = kwargs[name[0]]

    sorted_names = dict(sorted(names_with_ages.items()))
    string_to_return = ""
    for (name, age) in sorted_names.items():
        string_to_return += f"{name} is {age} years old.\n"

    return string_to_return
