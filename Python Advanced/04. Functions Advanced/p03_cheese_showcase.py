def sorting_cheeses(**cheeses):
    cheeses = dict(sorted(cheeses.items(), key= lambda d: (-len(d[1]), d[0])))

    joined_dict = []

    for (name, quantities) in cheeses.items():
        joined_dict.append(name)
        joined_dict += sorted(quantities, reverse=True)

    return "\n".join([str(x) for x in joined_dict])

# print(
#  sorting_cheeses(
#  Parmesan=[102, 120, 135],
#  Camembert=[100, 100, 105, 500, 430],
#  Mozzarella=[50, 125],
#  )
# )

# print(
#  sorting_cheeses(
#  Parmigiano=[165, 215],
#  Feta=[150, 515],
#  Brie=[150, 125]
#  )
# )
