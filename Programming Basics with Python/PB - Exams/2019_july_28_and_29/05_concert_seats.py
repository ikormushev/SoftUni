tickets_total = int(input())

english_alphabet_high = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
seat = ""

for i in range(1, tickets_total + 1):
    ticket_num = input()
    if len(ticket_num) == 4:
        if ticket_num[0] in english_alphabet_high:
            seat = f"{ticket_num[0]}{ticket_num[1]}{ticket_num[2]}"
        else:
            seat = f"{ticket_num[3]}{ticket_num[1]}{ticket_num[2]}"
    elif len(ticket_num) == 5 or len(ticket_num) == 6:
        seat = f"{ticket_num[0]}{ord(ticket_num[1])}"
    print(f"Seat decoded: {seat}")
