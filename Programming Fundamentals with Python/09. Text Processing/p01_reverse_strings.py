while True:
    given_string = input()
    if given_string == "end":
        break
    print(f"{given_string} = {given_string[::-1]}")
