from fibonacci_module.fibonacci_commands import create_sequence, locate_number

fibonacci_sequence = []

while True:
    command = input()
    if command == "Stop":
        print("--- Program end ---")
        break

    new_command = command.split()
    number = int(new_command[-1])

    if new_command[0] == "Create":
        fibonacci_sequence = create_sequence(number)
        print(*fibonacci_sequence)
    elif new_command[0] == "Locate":
        print(locate_number(fibonacci_sequence, number))
