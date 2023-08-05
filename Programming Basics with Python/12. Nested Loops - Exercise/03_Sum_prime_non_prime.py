prime_numbers_sum = 0
non_prime_numbers_sum = 0
prime_number = False

while True:
    command = input()
    if command == "stop":
        break
    number = int(command)

    if number < 0:
        print("Number is negative.")
    else:
        for i in range(2, number):
            if number % i == 0:
                prime_number = False
                break
            else:
                prime_number = True
        if prime_number or number == 2:
            prime_numbers_sum += number
        else:
            non_prime_numbers_sum += number

print(f"Sum of all prime numbers is: {prime_numbers_sum}")
print(f"Sum of all non prime numbers is: {non_prime_numbers_sum}")
