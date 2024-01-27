given_string = [[x for x in row.split()] for row in input().split("|")][::-1]

for row in range(len(given_string)):
    for col in range(len(given_string[row])):
        print(given_string[row][col], end=" ")
