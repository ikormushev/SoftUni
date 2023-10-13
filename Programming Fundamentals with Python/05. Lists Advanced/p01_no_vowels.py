text = list(input())

no_vowels_text = [x for x in text if x.lower() not in ['a', 'o', 'u', 'e', 'i']]
print("".join(no_vowels_text))
