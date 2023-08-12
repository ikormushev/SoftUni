gym_visitors_num = int(input())

activities = {
    "Back": 0,
    "Chest": 0,
    "Legs": 0,
    "Abs": 0,
    "Protein shake": 0,
    "Protein bar": 0
}

for i in range(1, gym_visitors_num + 1):
    activity = input()
    activities[activity] += 1

protein_buyers_num = activities["Protein shake"] + activities["Protein bar"]
people_working_out_num = gym_visitors_num - protein_buyers_num

protein_buyers_percentage = protein_buyers_num / gym_visitors_num * 100
people_working_out_percentage = people_working_out_num / gym_visitors_num * 100

print(f'{activities["Back"]} - back')
print(f'{activities["Chest"]} - chest')
print(f'{activities["Legs"]} - legs')
print(f'{activities["Abs"]} - absk')
print(f'{activities["Protein shake"]} - protein shake')
print(f'{activities["Protein bar"]} - protein bar')
print(f"{people_working_out_percentage:.2f}% - work out")
print(f"{protein_buyers_percentage:.2f}% - protein")
