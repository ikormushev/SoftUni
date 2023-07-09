vegetables_kg_bgn = float(input())
fruits_kg_bgn = float(input())
vegetables_kg = int(input())
fruits_kg = int(input())

eur_exchange_bgn = 1.94

vegetables_price = vegetables_kg_bgn * vegetables_kg
fruits_price = fruits_kg_bgn * fruits_kg

final_price = (vegetables_price + fruits_price) / eur_exchange_bgn

print('{:0.2f}'.format(final_price))
