animals = input()

animals_list = list(animals.split(", "))
position_wolf = 0
position_sheep = 0

for i in range(len(animals_list) + 1):
    if animals_list[-1] == "wolf":
        print("Please go away and stop eating my sheep")
        break

    if animals_list[-i] == "wolf":
        position_wolf = i
    elif animals_list[-i] == "sheep":
        position_sheep = i

    if position_wolf - position_sheep == 1:
        print(f"Oi! Sheep number {position_sheep}! You are about to be eaten by a wolf!")
        break
