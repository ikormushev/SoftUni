words = input().split(" ")
wanted_palindrome = input()

palindromes = [x for x in words if x == x[::-1]]
print(palindromes)

only_wanted_palindrome = [y for y in palindromes if y == wanted_palindrome]
print(f"Found palindrome {len(only_wanted_palindrome)} times")
