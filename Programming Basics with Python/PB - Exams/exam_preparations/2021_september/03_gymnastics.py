country = input()
equipment = input()

grades = {
    "Russia": {
        "ribbon": (9.100 + 9.400),
        "hoop": (9.300 + 9.800),
        "rope": (9.600 + 9.000)
    },
    "Bulgaria": {
        "ribbon": (9.600 + 9.400),
        "hoop": (9.550 + 9.750),
        "rope": (9.500 + 9.400)
    },
    "Italy": {
        "ribbon": (9.200 + 9.500),
        "hoop": (9.450 + 9.350),
        "rope": (9.700 + 9.150)
    }
}

grade = grades[country][equipment]
more_grades_needed = 20 - grade

print(f"The team of {country} get {grade:.3f} on {equipment}.")
print(f"{(more_grades_needed / 20 * 100):.2f}%")
