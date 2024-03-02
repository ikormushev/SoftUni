from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for given_product in self.products:
            if given_product.name == product_name:
                return given_product

    def remove(self, product_name: str):
        for given_product in self.products:
            if given_product.name == product_name:
                self.products.remove(given_product)
                break

    def __repr__(self):
        return "\n".join([f"{x.name}: {x.quantity}" for x in self.products])
