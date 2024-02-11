def create_sequence(count: int) -> list:
    sequence = []

    for i in range(count):
        if i == 0:
            sequence.append(0)
        elif i in [1, 2]:
            sequence.append(1)
        else:
            previous_two_numbers_sum = sequence[-1] + sequence[-2]
            sequence.append(previous_two_numbers_sum)

    return sequence


def locate_number(sequence: list, wanted_number: int) -> str:
    try:
        wanted_number_index = sequence.index(wanted_number)
        return f"The number - {wanted_number} is at index {wanted_number_index}."
    except ValueError:
        return f"The number {wanted_number} is not in the sequence!"
