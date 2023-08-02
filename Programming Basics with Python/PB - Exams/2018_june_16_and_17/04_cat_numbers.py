cats_num = int(input())

cat_unique_number = ""  # could be done with 4 unique variables, not just by adding each one as a string

for n in range(1, cats_num + 1):
    cat_unique_number = ""
    cat_first_name = input()
    cat_last_name = input()
    last_two_digits_birth = int(input())

    cat_unique_number += str(last_two_digits_birth)
    cat_unique_number += str(ord(cat_first_name[0]))
    cat_unique_number += str(ord(cat_last_name[0]))
    cat_unique_number += str(n)
    print(f"{cat_unique_number}")
