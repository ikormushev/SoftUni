ticket_types_num = {
    "student": 0,
    "standard": 0,
    "kid": 0
}

total_tickets = 0

while True:
    command = input()
    if command == "Finish":
        break
    movie_name = command
    seats = int(input())
    each_movie_tickets = 0
    while True:
        if seats == each_movie_tickets:
            break
        second_command = input()
        if second_command == "End":
            break
        ticket_type = second_command
        total_tickets += 1
        ticket_types_num[ticket_type] += 1
        each_movie_tickets += 1
    each_movie_tickets_p = each_movie_tickets / seats * 100
    print(f"{movie_name} - {each_movie_tickets_p:.2f}% full.")

ticket_students_p = ticket_types_num["student"] / total_tickets * 100
ticket_standard_p = ticket_types_num["standard"] / total_tickets * 100
ticket_kids_p = ticket_types_num["kid"] / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{ticket_students_p:.2f}% student tickets.")
print(f"{ticket_standard_p:.2f}% standard tickets.")
print(f"{ticket_kids_p:.2f}% kids tickets.")
