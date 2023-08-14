shipment_kg = float(input())
delivery_type = input()
distance_km = int(input())

kg_price = 0
price = 0

if shipment_kg < 1:
    kg_price = 0.03
    if delivery_type == "express":
        kg_price += (kg_price * 0.80) * shipment_kg
elif 1 <= shipment_kg < 10:
    kg_price = 0.05
    if delivery_type == "express":
        kg_price += (kg_price * 0.40) * shipment_kg
elif 10 <= shipment_kg < 40:
    kg_price = 0.10
    if delivery_type == "express":
        kg_price += (kg_price * 0.05) * shipment_kg
elif 40 <= shipment_kg < 90:
    kg_price = 0.15
    if delivery_type == "express":
        kg_price += (kg_price * 0.02) * shipment_kg
elif 90 <= shipment_kg <= 150:
    kg_price = 0.20
    if delivery_type == "express":
        kg_price += (kg_price * 0.01) * shipment_kg

price = distance_km * kg_price

print(f"The delivery of your shipment with weight of {shipment_kg:.3f} "
      f"kg. would cost {price:.2f} lv.")