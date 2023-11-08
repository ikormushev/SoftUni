import re


def winning_ticket(ticket, pattern):
    first_half = ticket[:int(len(ticket) / 2)]
    second_half = ticket[int(len(ticket) / 2):]
    if not (re.search(pattern, first_half) and re.search(pattern, second_half)):
        return False

    return True


def winning_symbols_length(ticket, pattern):
    first_half = ticket[:len(ticket) // 2]
    second_half = ticket[len(ticket) // 2:]
    first_half_length = min(re.findall(pattern, first_half), key=len)
    second_half_length = min(re.findall(pattern, second_half), key=len)
    return min(len(first_half_length), len(second_half_length))


tickets = re.split(r"\s*,\s+", input())

for i in range(len(tickets)):
    found_ticket = tickets[i]
    if len(found_ticket) == 20:
        # regex like [@#$^]{6,} will not work because it counts a case like $$$#$$$ as valid
        ticket_pattern = r"\@{6,}|\#{6,}|\${6,}|\^{6,}"
        if winning_ticket(found_ticket, ticket_pattern):
            winning_symbol = (re.search(ticket_pattern, found_ticket)).group()[0]
            winning_ticket_pattern = r"\@{10,}|\#{10,}|\${10,}|\^{10,}"
            if winning_ticket(found_ticket, winning_ticket_pattern):
                symbols_length = winning_symbols_length(found_ticket, winning_ticket_pattern)
                print(f"ticket \"{found_ticket}\" - {symbols_length}{winning_symbol} Jackpot!")
            else:
                symbols_length = winning_symbols_length(found_ticket, ticket_pattern)
                print(f"ticket \"{found_ticket}\" - {symbols_length}{winning_symbol}")
        else:
            print(f"ticket \"{found_ticket}\" - no match")
    else:
        print("invalid ticket")
