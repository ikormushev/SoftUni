airline_name = input()
tickets_adult_num = int(input())
tickets_kids_num = int(input())
tickets_adult_price = float(input())
use_fee = float(input())

tickets_adult = (tickets_adult_price + use_fee) * tickets_adult_num
tickets_kids = (tickets_adult_price * 0.30 + use_fee) * tickets_kids_num
total_price = tickets_adult + tickets_kids

profit = total_price * 0.20

print(f"The profit of your agency from {airline_name} tickets is {profit:.2f} lv.")
