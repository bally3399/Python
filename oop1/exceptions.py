class InvalidAmountException(Exception):

    def __init__(self, message):
        super().__init__(message)


class InsufficientFundsException(Exception):

    def __init__(self, message):
        super().__init__(message)


class InvalidPinException(Exception):

    def __init__(self, message):
        super().__init__(message)


class AccountNotFoundException(Exception):

    def __init__(self, message="account not found."):
        self.message = message
        super().__init__(self.message)


