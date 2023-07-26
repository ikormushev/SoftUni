planet_name = input()
days = int(input())

planets = ["Mercury", "Venus", "Mars",
           "Jupiter", "Saturn", "Uranus", "Neptune"]
planets_distance_from_earth = {
    "Mercury": 0.61,
    "Venus": 0.28,
    "Mars": 0.52,
    "Jupiter": 4.2,
    "Saturn": 8.52,
    "Uranus": 18.21,
    "Neptune": 29.09
}

planets_max_stay = {
    "Mercury": 7,
    "Venus": 14,
    "Mars": 20,
    "Jupiter": 5,
    "Saturn": 3,
    "Uranus": 3,
    "Neptune": 2
}

if planet_name not in planets:
    print("Invalid planet name!")
else:
    if days > planets_max_stay[planet_name]:
        print("Invalid number of days!")
    else:
        distance = planets_distance_from_earth[planet_name] * 2
        time_to_planet = 226 * planets_distance_from_earth[planet_name]
        days_taken = (time_to_planet * 2) + days
        print(f"Distance: {distance:.2f}")
        print(f"Total number of days: {days_taken:.2f}")
