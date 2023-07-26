bees_num = int(input())
flowers_num = int(input())

honey = flowers_num * 0.21 * bees_num
honeycombs_num = honey // 100
honey_left = honey % 100

print(f"{honeycombs_num:.0f} honeycombs filled.")
print(f"{honey_left:.2f} grams of honey left")
