text = input()

text_list = list(text)
indexes_list = []

for i in range(len(text_list)):
    if ord(text_list[i]) in range(ord("A"), ord("Z") + 1):
        indexes_list.append(i)

print(indexes_list)
