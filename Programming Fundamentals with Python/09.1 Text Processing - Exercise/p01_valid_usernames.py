def valid_symbol(symbol: str) -> bool:
    if symbol.isalpha():
        return True
    elif symbol.isnumeric():
        return True
    elif symbol in ["-", "_"]:
        return True
    return False


usernames = input().split(", ")

for username in usernames:
    if 3 <= len(username) <= 16:
        for letter in username:
            if not valid_symbol(letter):
                break
        else:
            print(username)
