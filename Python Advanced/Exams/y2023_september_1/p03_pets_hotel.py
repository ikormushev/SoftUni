def accommodate_new_pets(capacity: int, weight_limit: float, *args):
    pets = {}
    pets_not_accommodated = 0
    for (pet_type, pet_weight) in args:
        if capacity == 0:
            pets_not_accommodated += 1
            continue
        if pet_weight <= weight_limit:
            if pet_type not in pets:
                pets[pet_type] = 0
            pets[pet_type] += 1
            capacity -= 1

    string_to_print = ""
    if pets_not_accommodated:
        string_to_print += "You did not manage to accommodate all pets!\n"
    else:
        string_to_print += f"All pets are accommodated! Available capacity: {capacity}.\n"
    string_to_print += "Accommodated pets:\n"
    for (pet_type, pets_count) in sorted(pets.items(), key=lambda d: d[0]):
        string_to_print += f"{pet_type}: {pets_count}\n"

    return string_to_print
