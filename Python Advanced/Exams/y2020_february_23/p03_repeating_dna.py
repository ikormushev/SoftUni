def get_repeating_DNA(sequence):
    dna_sequences = {}
    dna_length = 10
    for i in range(len(sequence)):
        if dna_length + i <= len(sequence):
            current_sequence = sequence[i:dna_length + i]
            if current_sequence not in dna_sequences:
                dna_sequences[current_sequence] = 0
            dna_sequences[current_sequence] += 1
        else:
            break

    wanted_sequences = [seq for (seq, count) in dna_sequences.items() if count > 1]
    return wanted_sequences


test = "AAAAAACCCCAAAAAACCCCTTCAAAATCTTTCAAAATCT"

result = get_repeating_DNA(test)

print(result)

test = "TTCCTTAAGGCCGACTTCCAAGGTTCGATC"

result = get_repeating_DNA(test)

print(result)

test = "AAAAAAAAAAA"

result = get_repeating_DNA(test)

print(result)

