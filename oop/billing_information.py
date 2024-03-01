class BillingInformation:
    def __init__(self, phoneNumber, receiverName, deliveryAddress, creditCardInfo):
        self.phoneNumber = phoneNumber
        self.receiverName = receiverName
        self.deliveryAddress = deliveryAddress
        self.creditCardInfo = creditCardInfo

    def get_phone_number(self):
        return self.phoneNumber

    def get_receiver_name(self):
        return self.receiverName

    def get_delivery_address(self):
        return self.deliveryAddress

    def get_credit_card_info(self):
        return self.creditCardInfo

    def set_phone_number(self, phoneNumber):
        self.phoneNumber = phoneNumber

    def set_receiver_name(self, receiverName):
        self.receiverName = receiverName

    def set_delivery_address(self, deliveryAddress):
        self.deliveryAddress = deliveryAddress

    def set_credit_card_info(self, creditCardInfo):
        self.creditCardInfo = creditCardInfo
