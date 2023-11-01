
resources_collection = {}

while True:
    command = input()
    if command == "stop":
        break
    given_resource = command
    resource_quantity = int(input())

    if given_resource not in resources_collection:
        resources_collection[given_resource] = resource_quantity
    else:
        resources_collection[given_resource] += resource_quantity

[print(f"{r} -> {q}") for (r, q) in resources_collection.items()]
