shipment_kg = float(input())
service_type = input()
distance_kg = int(input())

price = 0

if service_type == "standard":
    if shipment_kg < 1:
        price = distance_kg * 0.03
    elif 1 <= shipment_kg <= 10:
        price = distance_kg * 0.05
    elif 11 <= shipment_kg <= 40:
        price = distance_kg * 0.10
    elif 41 <= shipment_kg <= 90:
        price = distance_kg * 0.15
    elif 91 <= shipment_kg <= 150:
        price = distance_kg * 0.20

if service_type == "express":
    if shipment_kg < 1:
        price = distance_kg * (0.03 * 1.8)
    elif 1 <= shipment_kg <= 10:
        price = distance_kg * (0.05 * 1.4)
    elif 11 <= shipment_kg <= 40:
        price = distance_kg * (0.10 * 1.05)
    elif 41 <= shipment_kg <= 90:
        price = distance_kg * (0.15 * 1.02)
    elif 91 <= shipment_kg <= 150:
        price = distance_kg * (0.20 * 1.01)

print(f"The delivery of your shipment with "
      f"weight of {shipment_kg:.3f} kg. would cost {price:.2f} lv.")
