flour_kg_price = float(input())
flour_kg = float(input())
sugar_kg = float(input())
eggs_num = int(input())
yeast_packets = int(input())

sugar_kg_price = flour_kg_price * 0.75
eggs_price = flour_kg_price * 1.10
yeast_price = sugar_kg_price * 0.20

flour = flour_kg * flour_kg_price
sugar = sugar_kg * sugar_kg_price
eggs = eggs_price * eggs_num
yeast = yeast_price * yeast_packets

total_price = flour + sugar + eggs + yeast

print(f"{total_price:.2f}")
