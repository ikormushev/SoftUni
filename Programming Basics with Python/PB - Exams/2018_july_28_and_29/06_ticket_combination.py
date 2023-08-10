combination_number = int(input())

combinations = 0
combination = ""
prize = 0
is_valid = False

for s1 in range(ord("B"), ord("M")):  # while it's nice to use ord("L") + 1, it bugs and doesn't give the right output
    if is_valid:
        break
    if s1 % 2 == 0:
        for s2 in range(ord("f"), ord("`"), -1):  # same here
            if is_valid:
                break
            for s3 in range(ord("A"), ord("D")):  # same here
                if is_valid:
                    break
                for s4 in range(1, 11):
                    if is_valid:
                        break
                    for s5 in range(10, 0, -1):
                        combination = f"{chr(s1)}{chr(s2)}{chr(s3)}{s4}{s5}"
                        combinations += 1
                        prize = s1+ s2 + s3 + s4 + s5
                        if combinations == combination_number:
                            is_valid = True
                            break
if is_valid:
    print(f"Ticket combination: {combination}")
    print(f"Prize: {prize} lv.")
