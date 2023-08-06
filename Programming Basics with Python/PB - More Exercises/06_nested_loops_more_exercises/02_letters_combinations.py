lower_letter_start = input()
lower_letter_end = input()
lower_letter_exclude = input()

combinations = 0

for l1 in range(ord(lower_letter_start), ord(lower_letter_end) + 1):
    if l1 == ord(lower_letter_exclude):
        continue
    for l2 in range(ord(lower_letter_start), ord(lower_letter_end) + 1):
        if l2 == ord(lower_letter_exclude):
            continue
        for l3 in range(ord(lower_letter_start), ord(lower_letter_end) + 1):
            if l3 == ord(lower_letter_exclude):
                continue
            print(f"{chr(l1)}{chr(l2)}{chr(l3)}", end=" ")
            combinations += 1
print(combinations)
