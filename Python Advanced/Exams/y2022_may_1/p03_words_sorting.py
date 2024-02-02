def words_sorting(*args):
    words = {}
    total_sum = 0
    for word in args:
        ascii_sum = sum([ord(x) for x in word])
        words[word] = ascii_sum
        total_sum += ascii_sum
    if total_sum % 2 == 1:
        words = dict(sorted(words.items(), key=lambda d: -d[1]))
    else:
        words = dict(sorted(words.items(), key=lambda d: d[0]))

    string_to_print = ""

    for (word, value) in words.items():
        string_to_print += f"{word} - {value}\n"

    return string_to_print


print(words_sorting('escape', 'charm', 'mythology'))

print(words_sorting('escape', 'charm', 'eye'))

print(words_sorting('cacophony', 'accolade'))
