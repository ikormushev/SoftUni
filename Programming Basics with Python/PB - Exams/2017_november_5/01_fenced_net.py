place_length = int(input())
place_width = int(input())
place_height = float(input())
net_price_m = float(input())
net_square_m_weight_kg = float(input())

net_length = 2 * (place_length + place_width) # net_length == place_perimeter
net_full_price = net_length * net_price_m

net_perimeter = net_length * place_height
net_weight = net_perimeter * net_square_m_weight_kg

print(net_length)
print(f"{net_full_price:.2f}")
print(f"{net_weight:.3f}")
