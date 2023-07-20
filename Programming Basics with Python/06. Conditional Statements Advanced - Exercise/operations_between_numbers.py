first_number = int(input())
second_number = int(input())
math_operator = input()

result = 0

if math_operator == "+":
    result = first_number + second_number
elif math_operator == "-":
    result = first_number - second_number
elif math_operator == "*":
    result = first_number * second_number


if math_operator == "+" or math_operator == "-" \
        or math_operator == "*":
    number_type = 0
    if result % 2 == 0:
        number_type = "even"
    else:
        number_type = "odd"
    print(f"{first_number} {math_operator} {second_number} "
          f"= {result} - {number_type}")

if math_operator == "/" or math_operator == "%":
    if second_number == 0:
        print(f"Cannot divide {first_number} by zero")
    else:
        if math_operator == "/":
            result = first_number / second_number
            print(f"{first_number} / {second_number} = {result:.2f}")
        elif math_operator == "%":
            result = first_number % second_number
            print(f"{first_number} % {second_number} = {result}")
