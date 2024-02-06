from collections import deque

matrix_size = 6

board = [input().split() for _ in range(matrix_size)]

hit_buckets = []

throws = deque()

for _ in range(3):
    throw = input().split(", ")
    throw_row = int(throw[0][1:])
    throw_col = int(throw[1][:-1])
    throws.append([throw_row, throw_col])

total_points = 0

while throws:
    current_row, current_col = throws.popleft()
    if 0 <= current_row < matrix_size and 0 <= current_col < matrix_size:
        if board[current_row][current_col] == "B" and [current_row, current_col] not in hit_buckets:
            hit_buckets.append([current_row, current_col])
            for i in range(matrix_size):
                current_element = board[i][current_col]
                if current_element.isnumeric():
                    total_points += int(current_element)

prize = ""

if 100 <= total_points <= 199:
    prize = "Football"
elif 200 <= total_points <= 299:
    prize = "Teddy Bear"
elif total_points >= 300:
    prize = "Lego Construction Set"

if prize:
    print(f"Good job! You scored {total_points} points, and you've won {prize}.")
else:
    print(f"Sorry! You need {100 - total_points} points more to win a prize.")
