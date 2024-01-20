number = int(input())

chemical_elements = set()

for _ in range(number):
    compounds = set(input().split())
    chemical_elements = chemical_elements | compounds

[print(x) for x in chemical_elements]
