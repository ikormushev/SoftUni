from math import ceil

breads_num = int(input())

total_sugar = 0
total_flour = 0

max_used_sugar = 0
max_used_flour = 0

for b in range(1, breads_num + 1):
    sugar_gr = int(input())
    flour_gr = int(input())

    if sugar_gr > max_used_sugar:
        max_used_sugar = sugar_gr
    if flour_gr > max_used_flour:
        max_used_flour = flour_gr

    total_sugar += sugar_gr
    total_flour += flour_gr

sugar_packets = ceil(total_sugar / 950)
flour_packets = ceil(total_flour / 750)

print(f"Sugar: {sugar_packets}")
print(f"Flour: {flour_packets}")
print(f"Max used flour is {max_used_flour} grams, "
      f"max used sugar is {max_used_sugar} grams.")
