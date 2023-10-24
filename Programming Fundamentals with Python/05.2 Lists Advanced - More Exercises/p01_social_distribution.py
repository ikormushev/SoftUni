population = list(map(int, input().split(", ")))
minimum_wealth = int(input())

if sum(population) < len(population) * minimum_wealth:
    print("No equal distribution possible")
else:
    for i in range(len(population)):
        if population[i] < minimum_wealth:
            needed_money = minimum_wealth - population[i]
            richest_person = max(population)
            if richest_person - needed_money >= minimum_wealth:
                population[i] += needed_money
                population[population.index(richest_person)] -= needed_money
    print(population)
