dungeons_room = input().split("|")

initial_health = 100
initial_bitcoins = 0

health = initial_health

for i in range(len(dungeons_room)):
    room_name = dungeons_room[i].split(" ")

    if "potion" in room_name:
        heal_amount = int(room_name[1])
        if health + heal_amount > initial_health:
            heal_amount = initial_health - health
            health = initial_health
        else:
            health += heal_amount
        print(f"You healed for {heal_amount} hp.")
        print(f"Current health: {health} hp.")

    elif "chest" in room_name:
        bitcoins_amount = int(room_name[1])
        initial_bitcoins += bitcoins_amount
        print(f"You found {bitcoins_amount} bitcoins.")

    else:
        monster_name = room_name[0]
        monster_attack = int(room_name[1])
        if health - monster_attack > 0:
            health -= monster_attack
            print(f"You slayed {monster_name}.")
        else:
            print(f"You died! Killed by {monster_name}.")
            print(f"Best room: {i + 1}")
            break
else:
    print("You've made it!"
          f"\nBitcoins: {initial_bitcoins}"
          f"\nHealth: {health}")
