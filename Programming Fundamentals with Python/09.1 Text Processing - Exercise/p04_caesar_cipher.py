encrypted_text = list(input())

decrypted_text = [chr(ord(x) + 3) for x in encrypted_text]

print("".join(decrypted_text))
