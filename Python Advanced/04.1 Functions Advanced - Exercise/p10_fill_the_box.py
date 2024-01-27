def fill_the_box(height, length, width, *args):
    def box_size():
        return height * length * width

    box = box_size()
    last_index = 0
    for i in range(len(args)):
        if args[i] == "Finish":
            break
        else:
            last_index = i
            box -= args[i]
            if box <= 0:
                break

    if box > 0:
        return f"There is free space in the box. You could put {box} more cubes."
    else:
        return f"No more free space! You have {sum(args[last_index+1:-1]) - box} more cubes."
