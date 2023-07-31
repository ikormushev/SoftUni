hidden_command = 0
letter_c, letter_o, letter_n = 0, 0, 0
whole_word = ""
word = ""
letters_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letters_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

while True:
    letter = input()
    secret_word_n, secret_word_c, secret_word_o = False, False, False
    if letter == "End":
        break
    if letter in letters_lower or letter in letters_upper:
        pass
    else:
        continue
    if letter == "c" and letter_c != 1:
        letter_c += 1
        secret_word_c = True
        hidden_command += 1
    elif letter == "o" and letter_o != 1:
        letter_o += 1
        secret_word_o = True
        hidden_command += 1
    elif letter == "n" and letter_n != 1:
        letter_n += 1
        secret_word_n = True
        hidden_command += 1
    if hidden_command == 3 and letter in ["c", "o", "n"]:
        letter_c, letter_o, letter_n = 0, 0, 0
        hidden_command = 0
        whole_word += word + " "
        word = ""
        continue
    if not secret_word_c and letter == "c":
        word += letter
    elif not secret_word_n and letter == "n":
        word += letter
    elif not secret_word_o and letter == "o":
        word += letter
    if letter not in ["c", "o", "n"]:
        word += letter

print(whole_word)
