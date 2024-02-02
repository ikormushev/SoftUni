def forecast(*args):
    weather_strength = {
        "Sunny": 1,
        "Cloudy": 2,
        "Rainy": 3
    }

    locations = {}
    for (location, weather) in args:
        locations[location] = {}
        locations[location]["strength"] = weather_strength[weather]
        locations[location]["weather"] = weather

    sorted_locations = dict(sorted(locations.items(), key=lambda d: (d[1]["strength"], d[0])))

    string_to_print = ""
    for (location, weather_info) in sorted_locations.items():
        string_to_print += f"{location} - {weather_info['weather']}\n"

    return string_to_print


print(forecast(("Sofia", "Sunny"), ("London", "Cloudy"), ("New York", "Sunny")))

print(forecast(("Beijing", "Sunny"), ("Hong Kong", "Rainy"),
               ("Tokyo", "Sunny"), ("Sofia", "Cloudy"), ("Peru", "Sunny"),
               ("Florence", "Cloudy"), ("Bourgas", "Sunny")))

print(forecast(("Tokyo", "Rainy"), ("Sofia", "Rainy")))
