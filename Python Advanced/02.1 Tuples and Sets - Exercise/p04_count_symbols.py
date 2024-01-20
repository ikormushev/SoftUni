text = tuple(input())

occurrences = {}

for symbol in text:
    if symbol not in occurrences:
        occurrences[symbol] = text.count(symbol)

sorted_dict = dict(sorted(occurrences.items()))

[print(f"{s}: {o} time/s") for s, o in sorted_dict.items()]
