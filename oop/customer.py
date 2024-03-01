class Customer:
    def __init__(self, billing_information, cart):
        self.billing_information = billing_information
        self.cart = cart

    def get_billing_information(self):
        return self.billing_information

    def get_cart(self):
        return self.cart

    def set_billing_information(self, billing_information):
        self.billing_information = billing_information

    def set_cart(self, cart):
        self.cart = cart
