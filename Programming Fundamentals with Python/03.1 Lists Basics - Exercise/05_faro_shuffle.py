cards = input().split(" ")
shuffles = int(input())

first_half_deck = []
second_half_deck = []

shuffles_left = shuffles
previous_deck = cards

while shuffles_left > 0:
    first_half_deck.clear()
    second_half_deck.clear()

    first_half_deck_index = 0
    second_half_deck_index = 0

    for z in range(int((len(cards) / 2))):
        first_half_deck.append(previous_deck[z])

    for k in range(int(len(cards) / 2), len(cards)):
        second_half_deck.append(previous_deck[k])

    for j in range(1, len(previous_deck) - 1):
        if j % 2 == 1:
            previous_deck[j] = second_half_deck[second_half_deck_index]
            second_half_deck_index += 1
        elif j % 2 == 0:
            first_half_deck_index += 1
            previous_deck[j] = first_half_deck[first_half_deck_index]

    shuffles_left -= 1

print(previous_deck)
