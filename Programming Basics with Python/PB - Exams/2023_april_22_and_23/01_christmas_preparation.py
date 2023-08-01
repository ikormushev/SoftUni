wrapping_paper_number = int(input())
rolls_fabric_num = int(input())
glue_lt = float(input())
discount = int(input()) / 100

wrapping_paper = wrapping_paper_number * 5.80
rolls_fabric = rolls_fabric_num * 7.20
glue = glue_lt * 1.20

price = wrapping_paper + rolls_fabric + glue
price *= 1 - discount

print(f"{price:.3f}")
