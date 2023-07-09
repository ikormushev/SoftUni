budget = float(input())
graphic_cards_num = int(input())
processors_num = int(input())
ram_memory_num = int(input())

graphic_card_price = 250
graphic_cards = graphic_cards_num * graphic_card_price

processors_price = graphic_cards * 0.35
processors = processors_num * processors_price

ram_memory_price = graphic_cards * 0.1
ram_memory = ram_memory_num * ram_memory_price

final_price = graphic_cards + processors + ram_memory

if graphic_cards_num > processors_num:
    discount = final_price * 0.15
    final_price = final_price - discount

money_difference = abs(final_price - budget)

if budget >= final_price:
    print(f"You have {money_difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {money_difference:.2f} leva more!")
