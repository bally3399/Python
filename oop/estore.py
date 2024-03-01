class Estore:
    def __init__(self, customer, seller, admin):
        self.customer = customer
        self.seller = seller
        self.admin = admin

    def get_customer(self):
        return self.customer

    def set_customer(self, customer):
        self.customer = customer

    def get_seller(self):
        return self.seller

    def set_seller(self, seller):
        self.seller = seller

    def get_admin(self):
        return self.admin

    def set_admin(self, admin):
        self.admin = admin
