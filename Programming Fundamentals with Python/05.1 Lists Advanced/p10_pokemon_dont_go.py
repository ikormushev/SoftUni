distances_to_pokemon = list(map(int, input().split(" ")))

removed_items_sum = 0

while len(distances_to_pokemon) > 0:
    index = int(input())
    element_at_index = 0

    if index < 0:
        element_at_index = distances_to_pokemon[0]
        distances_to_pokemon.pop(0)
        distances_to_pokemon.insert(0, distances_to_pokemon[-1])
    elif index > len(distances_to_pokemon) - 1:
        element_at_index = distances_to_pokemon[-1]
        distances_to_pokemon.pop(-1)
        distances_to_pokemon.append(distances_to_pokemon[0])
    else:
        element_at_index = distances_to_pokemon[index]
        distances_to_pokemon.pop(index)

    for i in range(len(distances_to_pokemon)):
        if distances_to_pokemon[i] <= element_at_index:
            distances_to_pokemon[i] += element_at_index
        else:
            distances_to_pokemon[i] -= element_at_index

    removed_items_sum += element_at_index

print(removed_items_sum)
