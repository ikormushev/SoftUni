def multiplication_of_characters(first_given_string, second_given_string):
    total_sum = 0
    for i in range(len(first_given_string)):
        if i < len(second_given_string):
            total_sum += (ord(first_given_string[i]) * ord(second_given_string[i]))
        else:
            total_sum += ord(first_given_string[i])
    return total_sum


first_string, second_string = input().split(" ")
result = 0
if len(first_string) >= len(second_string):
    result = multiplication_of_characters(first_string, second_string)
else:
    result = multiplication_of_characters(second_string, first_string)

print(result)
