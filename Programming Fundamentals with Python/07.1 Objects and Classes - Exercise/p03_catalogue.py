class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return [wanted_product for wanted_product in self.products if wanted_product[0] == first_letter]

    def __repr__(self):
        modified_catalogue = f"Items in the {self.name} catalogue:"
        sorted_products = sorted(self.products)
        for i in range(len(sorted_products)):
            modified_catalogue += f"\n{sorted_products[i]}"

        return modified_catalogue
