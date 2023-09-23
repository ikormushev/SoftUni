lines_num = int(input())

letters_sum = 0

for _ in range(lines_num):
    letter = input()
    letters_sum += ord(letter)

print(f"The sum equals: {letters_sum}")
