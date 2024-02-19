class Product:
    def __init__(self, productId, productName, price, productDescription, category):
        self.productId = productId
        self.productName = productName
        self.price = price
        self.productDescription = productDescription
        self.category = category

    def get_product_id(self):
        return self.productId

    def set_product_id(self, productId):
        self.productId = productId

    def get_product_name(self):
        return self.productName

    def set_product_name(self, productName):
        self.productName = productName

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_product_description(self):
        return self.productDescription

    def set_product_description(self, productDescription):
        self.productDescription = productDescription

    def get_category(self):
        return self.category

    def set_category(self, category):
        self.category = category
