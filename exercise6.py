class Test:
    def __init__(self):
        self._first_name = ""

    def first_name(self):
        return self._first_name

    def print_name(self):
        return name.upper()

    def __repr__(self):
        return f"name:{self.first_name}"


test = Test()
name = "baliqis"
print(test.print_name())
