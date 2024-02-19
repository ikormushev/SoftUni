def cookbook(*args):
    book = {}

    for info in args:
        recipe_name, cuisine, ingredients = info
        if cuisine not in book:
            book[cuisine] = {}
        book[cuisine][recipe_name] = ingredients

    sorted_book = dict(sorted(book.items(), key=lambda d: (-len(d[1].keys()), d[0])))

    string_to_print = ""

    for (cuisine, info) in sorted_book.items():
        string_to_print += f"{cuisine} cuisine contains {len(info.keys())} recipes:\n"
        sorted_recipes = dict(sorted(info.items()))
        for (recipe, ingredients) in sorted_recipes.items():
            string_to_print += f"  * {recipe} -> Ingredients: {', '.join(ingredients)}\n"

    return string_to_print


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))
print(cookbook(
    ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"])
    ))
print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))