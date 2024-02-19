from enum import Enum


class CardType(Enum):
    VISA = 1
    MASTERCARD = 2
    AMERICAN_EXPRESS = 3


class CardInformation:
    def __init__(self, cvv, cardExpirationDate, creditCardNumber, cardName, cardType):
        self.cvv = cvv
        self.cardExpirationDate = cardExpirationDate
        self.creditCardNumber = creditCardNumber
        self.cardName = cardName
        self.cardType = cardType

    def get_cvv(self):
        return self.cvv

    def get_card_expiration_date(self):
        return self.cardExpirationDate

    def get_credit_card_number(self):
        return self.creditCardNumber

    def get_card_name(self):
        return self.cardName

    def get_card_type(self):
        return self.cardType

    def set_cvv(self, cvv):
        self.cvv = cvv

    def set_card_expiration_date(self, cardExpirationDate):
        self.cardExpirationDate = cardExpirationDate

    def set_credit_card_number(self, creditCardNumber):
        self.creditCardNumber = creditCardNumber

    def set_card_name(self, cardName):
        self.cardName = cardName
