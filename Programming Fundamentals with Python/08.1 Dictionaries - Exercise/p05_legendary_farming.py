key_materials = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}

junk_materials = {}
legendary_item = ""
item_found = False

while not item_found:
    total_farming = input().split(" ")
    for i in range(0, len(total_farming), 2):
        material = total_farming[i + 1].lower()
        material_quantity = int(total_farming[i])

        if material in key_materials:
            key_materials[material] += material_quantity
        else:
            if material not in junk_materials:
                junk_materials[material] = material_quantity
            else:
                junk_materials[material] += material_quantity

        if key_materials["shards"] >= 250:
            key_materials["shards"] -= 250
            legendary_item = "Shadowmourne"
            item_found = True
            break
        elif key_materials["fragments"] >= 250:
            key_materials["fragments"] -= 250
            legendary_item = "Valanyr"
            item_found = True
            break
        elif key_materials["motes"] >= 250:
            key_materials["motes"] -= 250
            legendary_item = "Dragonwrath"
            item_found = True
            break

print(f"{legendary_item} obtained!")
[print(f"{key_mat}: {key_mat_quantity}") for (key_mat, key_mat_quantity) in key_materials.items()]
[print(f"{junk_mat}: {junk_mat_quantity}") for (junk_mat, junk_mat_quantity) in junk_materials.items()]
