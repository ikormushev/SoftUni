def grocery_store(**kwargs):
    sorted_dict = dict(sorted(kwargs.items(), key=lambda d: (-d[1], -len(d[0]), d[0])))
    string_to_return = ""

    for (product, quantity) in sorted_dict.items():
        string_to_return += f"{product}: {quantity}\n"
    return string_to_return
