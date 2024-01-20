number = int(input())

even_set = set()
odd_set = set()

for i in range(1, number + 1):
    name = list(input())
    letters_values = [ord(x) for x in name]
    letters_sum = sum(letters_values) // i
    even_set.add(letters_sum) if letters_sum % 2 == 0 else odd_set.add(letters_sum)

last_set = set()
if sum(even_set) == sum(odd_set):
    last_set = even_set | odd_set
elif sum(even_set) < sum(odd_set):
    last_set = odd_set - even_set
else:
    last_set = even_set ^ odd_set

print(*last_set, sep=", ")
