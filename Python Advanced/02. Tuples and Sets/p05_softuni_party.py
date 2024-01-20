guests_num = int(input())

codes_types = set()
for _ in range(guests_num):
    reservation_code = input()
    codes_types.add(reservation_code)

code = input()
while code != "END":
    codes_types.discard(code)  # does not raise an error if code is not present
    code = input()

guests_not_present = len(codes_types)
print(guests_not_present)

sorted_set = sorted(codes_types)
[print(vip) for vip in sorted_set]
