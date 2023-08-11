egg_size = input()
egg_color = input()
eggs_num = int(input())

eggs = {
    "Large": {
        "Red": 16,
        "Green": 12,
        "Yellow": 9
    },
    "Medium": {
        "Red": 13,
        "Green": 9,
        "Yellow": 7
    },
    "Small": {
        "Red": 9,
        "Green": 8,
        "Yellow": 5
    },
}

earnings = eggs[egg_size][egg_color] * eggs_num
earnings *= 0.65

print(f"{earnings:.2f} leva.")
