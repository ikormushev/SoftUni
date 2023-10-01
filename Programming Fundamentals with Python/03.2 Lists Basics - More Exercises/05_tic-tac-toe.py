first_line = list(map(int, input().split(" ")))
second_line = list(map(int, input().split(" ")))
third_line = list(map(int, input().split(" ")))


def first_player_win():
    first_win = False
    if first_line[0] == first_line[1] == first_line[2] == 1:
        first_win = True
    elif second_line[0] == second_line[1] == second_line[2] == 1:
        first_win = True
    elif third_line[0] == third_line[1] == third_line[2] == 1:
        first_win = True

    elif first_line[0] == second_line[0] == second_line[0] == 1:
        first_win = True
    elif first_line[1] == second_line[1] == third_line[1] == 1:
        first_win = True
    elif first_line[2] == second_line[2] == third_line[2] == 1:
        first_win = True

    elif first_line[0] == second_line[1] == third_line[2] == 1:
        first_win = True
    elif first_line[2] == second_line[1] == third_line[0] == 1:
        first_win = True

    return first_win


def second_player_win():
    second_win = False
    if first_line[0] == first_line[1] == first_line[2] == 2:
        second_win = True
    elif second_line[0] == second_line[1] == second_line[2] == 2:
        second_win = True
    elif third_line[0] == third_line[1] == third_line[2] == 2:
        second_win = True

    elif first_line[0] == second_line[0] == second_line[0] == 2:
        second_win = True
    elif first_line[1] == second_line[1] == third_line[1] == 2:
        second_win = True
    elif first_line[2] == second_line[2] == third_line[2] == 2:
        second_win = True

    elif first_line[0] == second_line[1] == third_line[2] == 2:
        second_win = True
    elif first_line[2] == second_line[1] == third_line[0] == 2:
        second_win = True

    return second_win


if first_player_win():
    print("First player won")
elif second_player_win():
    print("Second player won")
else:
    print("Draw!")
