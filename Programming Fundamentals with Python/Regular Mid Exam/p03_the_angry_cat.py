def valid_item_type(item:  str, item_price: int, compare: int) -> bool:
    if item == "cheap" and item_price < compare:
        return True
    elif item == "expensive" and item_price >= compare:
        return True
    return False


price_ratings = list(map(int, input().split(", ")))
entry_point = int(input())
items_type = input()

price_comparison = price_ratings[entry_point]

left_side_items = []
right_side_items = []

for i in range(len(price_ratings)):
    if i < entry_point:
        if valid_item_type(items_type, price_ratings[i], price_comparison):
            left_side_items.append(price_ratings[i])
    elif i > entry_point:
        if valid_item_type(items_type, price_ratings[i], price_comparison):
            right_side_items.append(price_ratings[i])

left_side_items_sum = sum(left_side_items)
right_side_items_sum = sum(right_side_items)

if left_side_items_sum >= right_side_items_sum:
    print(f"Left - {left_side_items_sum}")
else:
    print(f"Right - {right_side_items_sum}")
