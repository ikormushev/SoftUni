breads_num = int(input())
egg_boxes = int(input())
cookies_kg = int(input())

breads = breads_num * 3.20
eggs = egg_boxes * 4.35
cookies = cookies_kg * 5.40
egg_paint = egg_boxes * 12 * 0.15

total_price = breads + eggs + cookies + egg_paint

print(f"{total_price:.2f}")
