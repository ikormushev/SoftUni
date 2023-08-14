wrapping_paper_num = int(input())
cloth_num = int(input())
glue_lt = float(input())
discount = int(input()) / 100

wrapping_paper = wrapping_paper_num * 5.80
cloth = cloth_num * 7.20
glue = glue_lt * 1.20

total_price = wrapping_paper + cloth + glue
total_price *= 1 - discount

print(f"{total_price:.3f}")
