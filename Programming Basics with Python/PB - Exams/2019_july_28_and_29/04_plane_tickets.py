from sys import maxsize

fastest_flight = ""
fastest_flight_min = maxsize
fastest_flight_price = 0

while True:
    command = input()
    if command == "End":
        hours = fastest_flight_min // 60
        minutes = fastest_flight_min % 60
        print(f"Ticket found for flight {fastest_flight} costs "
              f"{fastest_flight_price:.2f} leva with "
              f"{hours}h {minutes}m stay")
        break
    ticket_num = command
    ticket_price_eur = float(input())
    min_stay = int(input())
    price = ticket_price_eur * 1.96

    if min_stay < fastest_flight_min:
        fastest_flight = ticket_num
        fastest_flight_price = price
        fastest_flight_min = min_stay
