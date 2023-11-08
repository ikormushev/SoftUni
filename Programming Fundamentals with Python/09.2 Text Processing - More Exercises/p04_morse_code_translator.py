morse_code = input().split(" | ")

morse_code_alphabet = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z"
}
secret_message = []

for word in morse_code:
    decrypted_message = ""
    letters = word.split(" ")
    for letter in letters:
        if letter != "":
            decrypted_message += morse_code_alphabet[letter]

    secret_message.append(decrypted_message)

print(*secret_message)
