computers_num = int(input())

ratings = {
    2: 0,
    3: 0.50,
    4: 0.70,
    5: 0.85,
    6: 1
}

total_ratings = 0
sales = 0

for _ in range(1, computers_num + 1):
    data = int(input())
    rating = data % 10
    possible_sales = data // 10

    possible_sales *= ratings[rating]
    total_ratings += rating
    sales += possible_sales

average_rating = total_ratings / computers_num

print(f"{sales:.2f}")
print(f"{average_rating:.2f}")
