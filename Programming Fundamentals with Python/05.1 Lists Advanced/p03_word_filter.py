text = input().split(" ")

text_even_length = [x for x in text if len(x) % 2 == 0]

for i in range(len(text_even_length)):
    print(text_even_length[i])
