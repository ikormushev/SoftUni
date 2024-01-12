from collections import deque

robots = input().split(";")
starting_time = [int(x) for x in input().split(":")]

robots_info = {}

for robot in robots:
    info = robot.split("-")
    name = info[0]
    processing_time = int(info[1])
    robots_info[name] = {}
    robots_info[name]["robot_processing_time"] = processing_time
    robots_info[name]["product"] = ""
    robots_info[name]["product_processing_time"] = 0


processed_products = []
products_line = deque()

while True:
    command = input()
    if command == "End":
        break
    products_line.append(command)

while products_line:
    starting_time[2] += 1
    if starting_time[2] == 60:
        starting_time[2] = 0
        starting_time[1] += 1

    if starting_time[1] == 60:
        starting_time[1] = 0
        starting_time[0] += 1

    if starting_time[0] == 24:
        starting_time[0] = 0

    product = products_line.popleft()

    for name in robots_info:
        if robots_info[name]["product"] != "":
            robots_info[name]["product_processing_time"] += 1
            if robots_info[name]["product_processing_time"] == robots_info[name]["robot_processing_time"]:
                robots_info[name]["product"] = ""
                robots_info[name]["product_processing_time"] = 0

        if robots_info[name]["product"] == "" and product:
            robots_info[name]["product"] = product
            robots_info[name]["product_processing_time"] = 0
            print(f"{name} - {product} [{starting_time[0]:02}:{starting_time[1]:02}:{starting_time[2]:02}]")
            product = ""

    if product:
        products_line.append(product)