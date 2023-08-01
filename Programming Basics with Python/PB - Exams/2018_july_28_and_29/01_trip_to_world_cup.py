tickets_going = float(input())
tickets_returning = float(input())
match_ticket = float(input())
matches_num = int(input())
discount = int(input()) / 100

plane_tickets = (tickets_going + tickets_returning) * 6
plane_tickets *= 1 - discount

final_price = plane_tickets + ((match_ticket * matches_num) * 6)
final_price_per_person = final_price / 6

print(f"Total sum: {final_price:.2f} lv.")
print(f"Each friend has to pay {final_price_per_person:.2f} lv.")
