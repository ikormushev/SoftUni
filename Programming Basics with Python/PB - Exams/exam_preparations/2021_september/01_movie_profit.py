movie_name = input()
days_num = int(input())
tickets_num = int(input())
ticket_price = float(input())
cinema_profit = int(input()) / 100

total_earnings = (tickets_num * ticket_price) * days_num
total_earnings *= 1 - cinema_profit

print(f"The profit from the movie {movie_name} is {total_earnings:.2f} lv.")
