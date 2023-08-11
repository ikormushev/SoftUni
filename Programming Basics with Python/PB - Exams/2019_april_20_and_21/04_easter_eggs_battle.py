first_player_starting_eggs = int(input())
second_player_starting_eggs = int(input())

first_player_eggs_left = first_player_starting_eggs
second_player_eggs_left = second_player_starting_eggs

while True:
    command = input()
    if command == "End":
        print(f"Player one has {first_player_eggs_left} eggs left.")
        print(f"Player two has {second_player_eggs_left} eggs left.")
        break
    winner = command
    if winner == "one":
        second_player_eggs_left -= 1
    elif winner == "two":
        first_player_eggs_left -= 1

    if first_player_eggs_left == 0:
        print(f"Player one is out of eggs. Player two "
              f"has {second_player_eggs_left} eggs left.")
        break
    elif second_player_eggs_left == 0:
        print(f"Player two is out of eggs. Player one "
              f"has {first_player_eggs_left} eggs left.")
        break
