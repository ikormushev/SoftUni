software_version = list(map(int, input().split(".")))


def next_version(version: list) -> list:
    if version[1] == 9 and version[2] == 9:
        version = [version[0] + 1, 0, 0]
    elif version[2] == 9:
        version[1] += 1
        version[2] = 0
    else:
        version[2] += 1

    return version


new_version = next_version(software_version)
print(".".join(map(str, new_version)))
