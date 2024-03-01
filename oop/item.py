class Item:
    def __init__(self, quantity_of_product, product):
        self.quantity_of_product = quantity_of_product
        self.product = product

    def get_quantity_Of_Product(self):
        return self.quantity_of_product

    def get_product(self):
        return self.product

    def set_quantity_of_product(self, quantity_of_product):
        self.quantity_of_product = quantity_of_product

    def set_product(self, product):
        self.product = product
        