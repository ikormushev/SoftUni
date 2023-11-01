countries = input().split(", ")
capitals = input().split(", ")

country_capitals = {country: capital for (country, capital) in zip(countries, capitals)}

[print(f"{con} -> {cap}") for (con, cap) in country_capitals.items()]
