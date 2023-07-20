screening = input()
rows_number = int(input())
columns_number = int(input())

seats = rows_number * columns_number
price = 0

if screening == "Premiere":
    price = seats * 12.00
elif screening == "Normal":
    price = seats * 7.50
elif screening == "Discount":
    price = seats * 5.00

print(f"{price:.2f} leva")
