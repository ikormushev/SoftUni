from collections import deque

given_strings = deque(input().split())

valid_colors = deque()
given_colors = {"red", "yellow", "blue", "orange", "purple", "green"}

while given_strings:
    first_part = given_strings.popleft()
    second_part = given_strings.pop() if given_strings else ""
    first_possible_color = first_part + second_part
    second_possible_color = second_part + first_part

    if first_possible_color in given_colors:
        valid_colors.append(first_possible_color)
    elif second_possible_color in given_colors:
        valid_colors.append(second_possible_color)
    else:
        first_part = first_part[:-1]
        second_part = second_part[:-1]
        if first_part:
            given_strings.insert(len(given_strings) // 2, first_part)
        if second_part:
            given_strings.insert(len(given_strings) // 2, second_part)

final_colors = []

while valid_colors:
    color_to_print = valid_colors.popleft()
    if color_to_print in ["red", "yellow", "blue"]:
        final_colors.append(color_to_print)
    elif color_to_print == "orange" and ({"red", "yellow"} <= (set(final_colors) | set(valid_colors))):
        final_colors.append(color_to_print)
    elif color_to_print == "purple" and ({"red", "blue"} <= (set(final_colors) | set(valid_colors))):
        final_colors.append(color_to_print)
    elif color_to_print == "green" and ({"yellow", "blue"} <= (set(final_colors) | set(valid_colors))):
        final_colors.append(color_to_print)

print(final_colors)
