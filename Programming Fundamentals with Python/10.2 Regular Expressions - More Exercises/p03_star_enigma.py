import re

decrypting_pattern = r"[starSTAR]"
message_pattern = (r"@(?P<planet>[a-zA-Z]+)[^\@\-\!\:\>]*"
                   r":(?P<population>\d+)[^\@\-\!\:\>]*"
                   r"!(?P<action>[AD])![^\@\-\!\:\>]*"
                   r"\-\>(?P<soldiers>\d+)")
messages_num = int(input())

planets_info = {
    "Attacked planets": [],
    "Destroyed planets": []
}

for _ in range(messages_num):
    encrypted_message = input()
    special_symbols_count = len(re.findall(decrypting_pattern, encrypted_message))
    decrypted_message = [chr(ord(x) - special_symbols_count) for x in encrypted_message]

    full_message = "".join(decrypted_message)
    if re.search(message_pattern, full_message) is None:
        continue

    message = (re.search(message_pattern, full_message)).groupdict()
    planet_name = message["planet"]
    action = message["action"]
    if action == "A":
        planets_info["Attacked planets"].append(planet_name)
    elif action == "D":
        planets_info["Destroyed planets"].append(planet_name)


for (attack_type, planets) in planets_info.items():
    print(f"{attack_type}: {len(planets)}")
    sorted_planets = sorted(planets)
    for planet in sorted_planets:
        print(f"-> {planet}")
