heroes_num = int(input())

heroes = {}
mana_points_limit = 200
hit_points_limit = 100

for _ in range(heroes_num):
    hero_info = input().split(" ")
    hero_name = hero_info[0]
    hero_hit_points = int(hero_info[1])
    hero_mana_points = int(hero_info[2])

    if hero_hit_points > hit_points_limit:
        hero_hit_points = hit_points_limit

    if hero_mana_points > mana_points_limit:
        hero_mana_points = mana_points_limit

    heroes[hero_name] = {}
    heroes[hero_name]["hit points"] = hero_hit_points
    heroes[hero_name]["mana points"] = hero_mana_points

while True:
    command = input()
    if command == "End":
        break
    action = command.split(" - ")
    action_type = action[0]
    hero = action[1]

    if action_type == "CastSpell":
        mana_needed = int(action[2])
        spell_name = action[3]
        if heroes[hero]["mana points"] >= mana_needed:
            heroes[hero]["mana points"] -= mana_needed
            print(f'{hero} has successfully cast {spell_name} and now has {heroes[hero]["mana points"]} MP!')
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")

    elif action_type == "TakeDamage":
        damage = int(action[2])
        attacker = action[3]
        heroes[hero]["hit points"] -= damage
        if heroes[hero]["hit points"] > 0:
            print(f'{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero]["hit points"]} HP left!')
        else:
            del heroes[hero]
            print(f"{hero} has been killed by {attacker}!")
    elif action_type == "Recharge":
        recharge_amount = int(action[2])
        if heroes[hero]["mana points"] + recharge_amount > mana_points_limit:
            recharge_amount = mana_points_limit - heroes[hero]["mana points"]
            heroes[hero]["mana points"] = mana_points_limit
        else:
            heroes[hero]["mana points"] += recharge_amount
        print(f'{hero} recharged for {recharge_amount} MP!')

    elif action_type == "Heal":
        recharge_amount = int(action[2])
        if heroes[hero]["hit points"] + recharge_amount > hit_points_limit:
            recharge_amount = hit_points_limit - heroes[hero]["hit points"]
            heroes[hero]["hit points"] = hit_points_limit
        else:
            heroes[hero]["hit points"] += recharge_amount
        print(f'{hero} healed for {recharge_amount} HP!')

for (name, stats) in heroes.items():
    print(name)
    print(f'  HP: {stats["hit points"]}')
    print(f'  MP: {stats["mana points"]}')
