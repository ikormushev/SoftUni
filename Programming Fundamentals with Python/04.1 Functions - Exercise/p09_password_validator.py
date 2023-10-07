password = input()


def is_length_valid(y):
    if len(y) < 6 or len(y) > 10:
        return False
    else:
        return True


def are_symbols_valid(x):
    for i in range(len(x)):
        if (ord(x[i]) in range(ord("0"), ord("9") + 1)
                or ord(x[i]) in range(ord("A"), ord("Z") + 1)
                or ord(x[i]) in range(ord("a"), ord("z") + 1)):
            continue
        else:
            return False
    else:
        return True


def are_there_at_least_two_digits(z):
    digits_count = 0
    for j in range(len(z)):
        if ord(z[j]) in range(ord("0"), ord("9") + 1):
            digits_count += 1

    if digits_count >= 2:
        return True
    else:
        return False


if not is_length_valid(password):
    print("Password must be between 6 and 10 characters")
if not are_symbols_valid(password):
    print("Password must consist only of letters and digits")
if not are_there_at_least_two_digits(password):
    print("Password must have at least 2 digits")

if (is_length_valid(password)
        and are_symbols_valid(password)
        and are_there_at_least_two_digits(password)):
    print("Password is valid")
