def start_spring(**kwargs):
    spring_objects = {}

    for (name, object_type) in kwargs.items():
        if object_type not in spring_objects:
            spring_objects[object_type] = []
        spring_objects[object_type].append(name)

    sorted_spring_objects = dict(sorted(spring_objects.items(), key=lambda d: (-len(d[1]), d[0])))

    for (object_type, names) in sorted_spring_objects.items():
        sorted_names = sorted(names)
        sorted_spring_objects[object_type] = sorted_names

    string_to_print = ""
    for (object_type, names) in sorted_spring_objects.items():
        string_to_print += f"{object_type}:\n"
        for name in names:
            string_to_print += f"-{name}\n"

    return string_to_print


example_objects = {"Water Lilly": "flower", "Swifts": "bird",
                   "Callery Pear": "tree", "Swallows": "bird",
                   "Dahlia": "flower", "Tulip": "flower"}
print(start_spring(**example_objects))

example_objects = {"Swallow": "bird", "Thrushes": "bird",
                   "Woodpeckers": "bird", "Swallows": "bird",
                   "Warblers": "bird", "Shrikes": "bird"}
print(start_spring(**example_objects))

example_objects = {"Magnolia": "tree", "Swallow": "bird",
                   "Thrushes": "bird", "Pear": "tree",
                   "Cherries": "tree", "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))

