pens_num = int(input())
markers_num = int(input())
cleaner_lt = float(input())
discount = int(input()) / 100

pens_price = pens_num * 5.80
markers_price = markers_num * 7.20
cleaner_price = cleaner_lt * 1.20

total_price = pens_price + markers_price + cleaner_price
total_price *= 1 - discount

print(f"{total_price:.3f}")
