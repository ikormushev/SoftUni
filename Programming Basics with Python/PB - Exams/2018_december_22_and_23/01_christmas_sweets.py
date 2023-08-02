baklava_kg_price = float(input())
muffins_kg_price = float(input())
stollen_kg = float(input())
candies_kg = float(input())
biscuits_kg = int(input())

stollen_kg_price = baklava_kg_price * 1.60
candies_kg_price = muffins_kg_price * 1.80
biscuits_kg_price = 7.50

stollen = stollen_kg * stollen_kg_price
candies = candies_kg * candies_kg_price
biscuits = biscuits_kg * biscuits_kg_price

price = stollen + candies + biscuits

print(f"{price:.2f}")
