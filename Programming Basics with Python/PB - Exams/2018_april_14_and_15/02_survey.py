votes = int(input())
votes_first_lang = int(input())

votes_second_lang = votes_first_lang * 0.80
votes_third_lang = votes_second_lang * 0.90

votes_first_three_lang = votes_first_lang + votes_second_lang + \
                         votes_third_lang

votes_diff = abs((votes / 2) - votes_first_three_lang)

if votes_first_three_lang >= (votes / 2):
    print(f"First three languages have {votes_diff:.0f} votes more")
else:
    print(f"First three languages have {votes_diff:.0f} votes less of half votes")
