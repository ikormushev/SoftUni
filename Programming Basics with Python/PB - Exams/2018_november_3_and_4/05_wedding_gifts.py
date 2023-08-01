guests_num = int(input())
gifts_num = int(input())

gift_types = {  # money, electrical appliances, vouchers, other
    "A": 0,
    "B": 0,
    "V": 0,
    "G": 0
}

for _ in range(1, gifts_num + 1):
    gift_type = input()
    gift_types[gift_type] += 1

a_percentage = gift_types["A"] / gifts_num * 100
b_percentage = gift_types["B"] / gifts_num * 100
v_percentage = gift_types["V"] / gifts_num * 100
g_percentage = gift_types["G"] / gifts_num * 100
guests_giving_gifts_percentage = gifts_num / guests_num * 100

print(f"{a_percentage:.2f}%")
print(f"{b_percentage:.2f}%")
print(f"{v_percentage:.2f}%")
print(f"{g_percentage:.2f}%")
print(f"{guests_giving_gifts_percentage:.2f}%")
