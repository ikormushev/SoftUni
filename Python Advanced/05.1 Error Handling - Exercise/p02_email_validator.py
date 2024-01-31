class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


valid_domains = (".com", ".bg", ".org", ".net")
name_min_length = 4
email = input()

while email != "End":
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")
    elif (len(email.split("@")[0])) <= name_min_length:
        raise NameTooShortError("Name must be more than 4 characters")
    elif ("." + email.split(".")[-1]) not in valid_domains:
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join(valid_domains)}")
    else:
        print("Email is valid")

    email = input()
