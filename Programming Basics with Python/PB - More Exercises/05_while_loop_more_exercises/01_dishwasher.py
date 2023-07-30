detergent_bottles_num = int(input())

detergent_ml = detergent_bottles_num * 750
loading_in_num = 0
plates_num = 0
pots_num = 0
detergent = detergent_ml

while detergent >= 0:
    data = input()
    if data == "End":
        break
    loading_in_num += 1
    dishes = int(data)
    if loading_in_num % 3 == 0:
        pots_num += dishes
        detergent -= (dishes * 15)
    else:
        plates_num += dishes
        detergent -= (dishes * 5)

if detergent >= 0:
    print("Detergent was enough!")
    print(f"{plates_num} dishes and {pots_num} pots were washed.")
    print(f"Leftover detergent {detergent} ml.")
else:
    print(f"Not enough detergent, {abs(detergent)} ml. more necessary!")
